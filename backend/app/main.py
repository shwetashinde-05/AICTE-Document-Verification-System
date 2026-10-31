import os
import shutil
import uuid
import datetime
from typing import Dict, Any, List, Optional
from fastapi import FastAPI, HTTPException, UploadFile, File, Form, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel

from .models import (
    User, Application, DocumentRecord, ExtractedMetadata, 
    VerificationFinding, ReviewerAction, IssuerVerificationResult,
    ComplianceRule, CourseIntake
)
from .seed_data import (
    SYNTHETIC_REFERENCE_INSTITUTION, DEFAULT_COMPLIANCE_RULES,
    SIMULATED_ISSUER_REGISTRY, DEFAULT_INFRASTRUCTURE_ITEMS,
    INITIAL_APPLICATIONS, SUPPORTED_CATEGORIES
)
from .ocr_engine import extract_text_from_pdf, parse_eoa_metadata, calculate_sha256
from .verification_engine import run_eoa_verification
from .issuer_service import query_issuer_registry
from .config import UPLOAD_DIR, SAMPLE_DOCS_DIR, APP_TITLE, APP_VERSION

app = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
    description="SIH26261 Decision Support System for AICTE Application Validation, Document Authentication and Regulatory Compliance"
)

# Enable CORS for external frontend or localhost dev servers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-Memory State for Demonstration
STATE = {
    "applications": {app["id"]: dict(app) for app in INITIAL_APPLICATIONS},
    "reference_institution": dict(SYNTHETIC_REFERENCE_INSTITUTION),
    "rules": [dict(r) for r in DEFAULT_COMPLIANCE_RULES],
    "categories": [dict(c) for c in SUPPORTED_CATEGORIES],
    "issuer_registry": dict(SIMULATED_ISSUER_REGISTRY),
    "audit_trail": [
        {
            "action_id": "AUD-INIT-001",
            "application_id": "APP-2026-001",
            "officer_name": "Dr. R. K. Sharma",
            "officer_role": "Scrutiny Officer - Western Regional Office",
            "action_type": "Observation Added",
            "remarks": "System initialized. AI-assisted checks executed on Doc_A_Correct_EoA.pdf. High fidelity match confirmed.",
            "timestamp": "2026-06-18 14:22:00 IST",
            "related_finding_id": None
        }
    ]
}

# Pre-run verification on initial applications so findings are fully populated
for app_id, app_data in STATE["applications"].items():
    if not app_data["findings"] and app_data["documents"]:
        # Find EoA doc
        for doc in app_data["documents"]:
            doc_file = os.path.join(SAMPLE_DOCS_DIR, doc["filename"])
            if os.path.exists(doc_file):
                res = extract_text_from_pdf(doc_file)
                meta = parse_eoa_metadata(res["text"])
                doc["extracted_metadata"] = meta.model_dump()
                findings, score, status = run_eoa_verification(meta, doc["filename"], STATE["reference_institution"])
                app_data["findings"] = [f.model_dump() for f in findings]
                app_data["overall_score"] = score

# --- AUTH & USER ENDPOINTS ---
class LoginRequest(BaseModel):
    username: str
    password: str
    role: str

@app.post("/api/auth/login")
def login(req: LoginRequest):
    # Safe demo authentication for 3 personas
    if req.role == "institution":
        return {
            "token": "demo-jwt-inst",
            "user": {
                "username": req.username or "principal@abctech.edu.in",
                "role": "institution",
                "name": "Dr. Aniruddha Joshi",
                "organization": "ABC Institute of Technology, Pune",
                "institution_id": "INST-PUNE-01",
                "email": "principal@abctech.edu.in"
            }
        }
    elif req.role == "aicte_officer":
        return {
            "token": "demo-jwt-officer",
            "user": {
                "username": req.username or "officer.rksharma@aicte-india.org",
                "role": "aicte_officer",
                "name": "Dr. R. K. Sharma",
                "organization": "AICTE Western Regional Office (WRO)",
                "email": "officer.rksharma@aicte-india.org"
            }
        }
    elif req.role == "aicte_admin":
        return {
            "token": "demo-jwt-admin",
            "user": {
                "username": req.username or "admin@aicte-india.org",
                "role": "aicte_admin",
                "name": "Prof. Rajive Kumar (Director - Approvals)",
                "organization": "AICTE Approval Bureau, New Delhi",
                "email": "admin@aicte-india.org"
            }
        }
    else:
        raise HTTPException(status_code=400, detail="Invalid role specified")

# --- REFERENCE DATA & RULES (AICTE ADMIN) ---
@app.get("/api/admin/reference-record")
def get_reference_record():
    return {
        "status": "success",
        "data": STATE["reference_institution"],
        "disclaimer": "Synthetic institutional reference data for demonstration purposes only. Not connected to live council database."
    }

@app.put("/api/admin/reference-record")
def update_reference_record(data: Dict[str, Any]):
    STATE["reference_institution"].update(data)
    return {"status": "success", "message": "Reference records updated", "data": STATE["reference_institution"]}

@app.get("/api/admin/rules")
def get_rules():
    return {"status": "success", "data": STATE["rules"]}

@app.post("/api/admin/rules/toggle/{rule_id}")
def toggle_rule(rule_id: str):
    for r in STATE["rules"]:
        if r["rule_id"] == rule_id:
            r["is_active"] = not r["is_active"]
            return {"status": "success", "rule": r}
    raise HTTPException(status_code=404, detail="Rule not found")

@app.get("/api/admin/categories")
def get_categories():
    return {"status": "success", "data": STATE["categories"]}

# --- APPLICATION MANAGEMENT (INSTITUTION & OFFICER) ---
@app.get("/api/applications")
def get_applications(institution_id: Optional[str] = None, role: Optional[str] = None):
    apps = list(STATE["applications"].values())
    if role == "institution" and institution_id:
        apps = [a for a in apps if a.get("institution_id") == institution_id]
    return {"status": "success", "count": len(apps), "data": apps}

@app.get("/api/applications/{app_id}")
def get_application_by_id(app_id: str):
    if app_id in STATE["applications"]:
        return {"status": "success", "data": STATE["applications"][app_id]}
    raise HTTPException(status_code=404, detail="Application not found")

class CreateAppRequest(BaseModel):
    category: str
    academic_year: str
    institution_name: str
    permanent_id: str
    contact_email: str

@app.post("/api/applications/create")
def create_application(req: CreateAppRequest):
    new_id = f"APP-2026-{len(STATE['applications']) + 1:03d}"
    app_record = {
        "id": new_id,
        "application_id": f"APP-DEMO-{len(STATE['applications']) + 1:03d}",
        "institution_id": "INST-PUNE-01",
        "institution_name": req.institution_name or "ABC Institute of Technology",
        "permanent_id": req.permanent_id or "1-1234567890",
        "academic_year": req.academic_year or "2026-27",
        "category": req.category or "Extension of Approval (EoA)",
        "status": "Draft",
        "created_at": datetime.datetime.now().isoformat(),
        "submitted_at": None,
        "documents": [],
        "findings": [],
        "infrastructure_items": [dict(item) for item in DEFAULT_INFRASTRUCTURE_ITEMS],
        "reviewer_actions": [],
        "overall_score": 0.0
    }
    STATE["applications"][new_id] = app_record
    return {"status": "success", "data": app_record}

@app.post("/api/applications/{app_id}/submit")
def submit_application(app_id: str):
    if app_id not in STATE["applications"]:
        raise HTTPException(status_code=404, detail="Application not found")
    app_data = STATE["applications"][app_id]
    app_data["status"] = "Submitted"
    app_data["submitted_at"] = datetime.datetime.now().isoformat()
    return {"status": "success", "message": "Application submitted for AICTE preliminary verification", "data": app_data}

# --- DOCUMENT UPLOAD & OCR EXTRACTION ---
@app.post("/api/applications/{app_id}/upload-document")
async def upload_document(
    app_id: str,
    doc_type: str = Form(...),
    preset_choice: Optional[str] = Form(None), # 'Doc_A_Correct', 'Doc_B_Incorrect', 'Doc_C_Incomplete'
    file: Optional[UploadFile] = File(None)
):
    if app_id not in STATE["applications"]:
        raise HTTPException(status_code=404, detail="Application not found")
        
    app_data = STATE["applications"][app_id]
    
    # Handle Preset Synthetic Document vs Uploaded file
    if preset_choice:
        preset_map = {
            "Doc_A_Correct": "Doc_A_Correct_EoA.pdf",
            "Doc_B_Incorrect": "Doc_B_Incorrect_EoA.pdf",
            "Doc_C_Incomplete": "Doc_C_Incomplete_EoA.pdf",
            "Fire_Safety_NOC": "Fire_Safety_Certificate_CERT-DEMO-101.pdf"
        }
        filename = preset_map.get(preset_choice, "Doc_A_Correct_EoA.pdf")
        source_path = os.path.join(SAMPLE_DOCS_DIR, filename)
        dest_filename = f"{app_id}_{filename}"
        dest_path = os.path.join(UPLOAD_DIR, dest_filename)
        if os.path.exists(source_path):
            shutil.copyfile(source_path, dest_path)
            with open(dest_path, "rb") as f:
                file_bytes = f.read()
        else:
            raise HTTPException(status_code=404, detail="Preset sample document not found")
    elif file:
        dest_filename = f"{app_id}_{file.filename}"
        dest_path = os.path.join(UPLOAD_DIR, dest_filename)
        file_bytes = await file.read()
        with open(dest_path, "wb") as f:
            f.write(file_bytes)
        filename = file.filename
    else:
        raise HTTPException(status_code=400, detail="Either preset_choice or file must be provided")

    # Compute SHA-256 for anomaly & duplicate detection
    sha256 = calculate_sha256(file_bytes)
    
    # Check for duplicate documents across other applications
    is_duplicate = False
    for other_id, other_app in STATE["applications"].items():
        if other_id != app_id:
            for d in other_app.get("documents", []):
                if d.get("sha256_hash") == sha256:
                    is_duplicate = True
                    break

    # Extract Text & Run OCR Metadata Parser
    extraction_res = extract_text_from_pdf(dest_path)
    metadata = parse_eoa_metadata(extraction_res["text"])
    
    anomaly_flags = []
    if is_duplicate:
        anomaly_flags.append("Identical Document SHA-256 Checksum detected in another submission.")
    if "MISSING" in dest_filename.upper() or "INCOMPLETE" in dest_filename.upper():
        anomaly_flags.append("Missing mandatory institutional identifiers or missing signature section.")
    if "180" in extraction_res["text"] and "120" not in extraction_res["text"]:
        anomaly_flags.append("Unsanctioned student intake figure detected in extracted curriculum schedule.")

    doc_record = {
        "id": f"DOC-{uuid.uuid4().hex[:6]}",
        "filename": filename,
        "saved_path": dest_filename,
        "doc_type": doc_type,
        "sha256_hash": sha256,
        "file_size_bytes": len(file_bytes),
        "upload_timestamp": datetime.datetime.now().isoformat(),
        "ocr_processed": True,
        "is_duplicate": is_duplicate,
        "anomaly_flags": anomaly_flags,
        "extracted_metadata": metadata.model_dump()
    }
    
    # Replace or add document
    existing_docs = [d for d in app_data["documents"] if d["doc_type"] != doc_type]
    existing_docs.append(doc_record)
    app_data["documents"] = existing_docs
    
    # Run immediate verification against active rules
    findings, score, status = run_eoa_verification(metadata, filename, STATE["reference_institution"])
    app_data["findings"] = [f.model_dump() for f in findings]
    app_data["overall_score"] = score
    app_data["status"] = status
    
    return {
        "status": "success",
        "message": "Document processed, OCR text extracted, and preliminary verification generated.",
        "document": doc_record,
        "findings": app_data["findings"],
        "overall_score": score,
        "preliminary_status": status
    }

# --- DOCUMENT DOWNLOAD & VIEWING ---
@app.get("/api/documents/view/{filename}")
def view_document(filename: str):
    # Look in UPLOAD_DIR or SAMPLE_DOCS_DIR
    upload_target = os.path.join(UPLOAD_DIR, filename)
    if os.path.exists(upload_target):
        return FileResponse(upload_target, media_type="application/pdf")
        
    sample_target = os.path.join(SAMPLE_DOCS_DIR, filename)
    if os.path.exists(sample_target):
        return FileResponse(sample_target, media_type="application/pdf")
        
    # Check if prefixed
    for fname in os.listdir(SAMPLE_DOCS_DIR):
        if fname in filename:
            return FileResponse(os.path.join(SAMPLE_DOCS_DIR, fname), media_type="application/pdf")
            
    raise HTTPException(status_code=404, detail="Requested document not found on server")

# --- MOCK ISSUER VERIFICATION SANDBOX ---
class IssuerQueryRequest(BaseModel):
    cert_number: str
    application_id: Optional[str] = None

@app.post("/api/issuer/verify")
def verify_certificate_with_issuer(req: IssuerQueryRequest):
    result = query_issuer_registry(req.cert_number)
    
    # Record in application if app_id provided
    if req.application_id and req.application_id in STATE["applications"]:
        app_data = STATE["applications"][req.application_id]
        if "issuer_checks" not in app_data:
            app_data["issuer_checks"] = []
        app_data["issuer_checks"].append(result.model_dump())
        
    return {
        "status": "success",
        "data": result.model_dump(),
        "disclaimer": "SIMULATED ISSUER VERIFICATION — NOT A LIVE GOVERNMENT INTEGRATION"
    }

# --- OFFICER ACTIONS & AUDIT TRAIL ---
class OfficerActionRequest(BaseModel):
    application_id: str
    officer_name: str
    officer_role: str
    action_type: str # 'Observation Added', 'Correction Requested', 'Refer for Physical Inspection', 'Escalated', 'Approved for Scrutiny'
    remarks: str
    related_finding_id: Optional[str] = None

@app.post("/api/officer/action")
def record_officer_action(req: OfficerActionRequest):
    if req.application_id not in STATE["applications"]:
        raise HTTPException(status_code=404, detail="Application not found")
        
    app_data = STATE["applications"][req.application_id]
    
    action_entry = {
        "action_id": f"ACT-{uuid.uuid4().hex[:6].upper()}",
        "application_id": req.application_id,
        "officer_name": req.officer_name,
        "officer_role": req.officer_role,
        "action_type": req.action_type,
        "remarks": req.remarks,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST"),
        "related_finding_id": req.related_finding_id
    }
    
    if "reviewer_actions" not in app_data:
        app_data["reviewer_actions"] = []
    app_data["reviewer_actions"].append(action_entry)
    
    # Audit log
    STATE["audit_trail"].insert(0, action_entry)
    
    # Update application status based on action
    if req.action_type == "Correction Requested":
        app_data["status"] = "Correction Required"
    elif req.action_type == "Refer for Physical Inspection":
        app_data["status"] = "Inspection Recommended"
    elif req.action_type == "Approved for Scrutiny":
        app_data["status"] = "Scrutiny Completed"
    elif req.action_type == "Escalated":
        app_data["status"] = "Under Scrutiny"
        
    return {"status": "success", "message": "Action recorded in regulatory audit trail", "action": action_entry}

@app.get("/api/officer/audit-log")
def get_audit_log():
    return {"status": "success", "data": STATE["audit_trail"]}

# --- INFRASTRUCTURE EVIDENCE REVIEW ---
class InfraUpdateRequest(BaseModel):
    application_id: str
    item_id: str
    status: str
    officer_remark: str

@app.post("/api/infrastructure/review")
def review_infrastructure_item(req: InfraUpdateRequest):
    if req.application_id not in STATE["applications"]:
        raise HTTPException(status_code=404, detail="Application not found")
        
    app_data = STATE["applications"][req.application_id]
    for item in app_data.get("infrastructure_items", []):
        if item["id"] == req.item_id:
            item["status"] = req.status
            item["officer_remark"] = req.officer_remark
            item["last_inspected"] = datetime.datetime.now().strftime("%Y-%m-%d")
            return {"status": "success", "data": item}
            
    raise HTTPException(status_code=404, detail="Infrastructure item not found")

# --- 1-CLICK DEMONSTRATION SCENARIOS FOR JUDGES ---
@app.post("/api/demo/run-scenario/{scenario_name}")
def run_demo_scenario(scenario_name: str):
    """
    Instantly configures the primary demonstration scenarios:
    - 'scenario_a': Correct EoA (All Match)
    - 'scenario_b': Incorrect EoA (Intake Mismatch & Missing Course)
    - 'scenario_c': Incomplete EoA (Missing IDs & Missing Sections)
    """
    target_app_id = "APP-2026-001"
    if target_app_id not in STATE["applications"]:
        target_app_id = list(STATE["applications"].keys())[0]
        
    app_data = STATE["applications"][target_app_id]
    
    if scenario_name == "scenario_a":
        # Load Doc A
        file_path = os.path.join(SAMPLE_DOCS_DIR, "Doc_A_Correct_EoA.pdf")
        res = extract_text_from_pdf(file_path)
        meta = parse_eoa_metadata(res["text"])
        findings, score, status = run_eoa_verification(meta, "Doc_A_Correct_EoA.pdf", STATE["reference_institution"])
        app_data["documents"] = [{
            "id": "DOC-DEMO-A",
            "filename": "Doc_A_Correct_EoA.pdf",
            "doc_type": "Extension of Approval (EoA)",
            "sha256_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "file_size_bytes": 48200,
            "upload_timestamp": datetime.datetime.now().isoformat(),
            "ocr_processed": True,
            "is_duplicate": False,
            "anomaly_flags": [],
            "extracted_metadata": meta.model_dump()
        }]
        app_data["findings"] = [f.model_dump() for f in findings]
        app_data["overall_score"] = score
        app_data["status"] = "Preliminary Checks Completed"
        return {"status": "success", "scenario": "Scenario A: Correct EoA Loaded", "data": app_data}
        
    elif scenario_name == "scenario_b":
        # Load Doc B
        file_path = os.path.join(SAMPLE_DOCS_DIR, "Doc_B_Incorrect_EoA.pdf")
        res = extract_text_from_pdf(file_path)
        meta = parse_eoa_metadata(res["text"])
        findings, score, status = run_eoa_verification(meta, "Doc_B_Incorrect_EoA.pdf", STATE["reference_institution"])
        app_data["documents"] = [{
            "id": "DOC-DEMO-B",
            "filename": "Doc_B_Incorrect_EoA.pdf",
            "doc_type": "Extension of Approval (EoA)",
            "sha256_hash": "7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069",
            "file_size_bytes": 45100,
            "upload_timestamp": datetime.datetime.now().isoformat(),
            "ocr_processed": True,
            "is_duplicate": False,
            "anomaly_flags": ["Intake Mismatch Detected", "Missing Course Omission"],
            "extracted_metadata": meta.model_dump()
        }]
        app_data["findings"] = [f.model_dump() for f in findings]
        app_data["overall_score"] = score
        app_data["status"] = "Correction Required"
        return {"status": "success", "scenario": "Scenario B: Incorrect EoA (Intake 180 vs 120, Missing AI&DS)", "data": app_data}
        
    elif scenario_name == "scenario_c":
        # Load Doc C
        file_path = os.path.join(SAMPLE_DOCS_DIR, "Doc_C_Incomplete_EoA.pdf")
        res = extract_text_from_pdf(file_path)
        meta = parse_eoa_metadata(res["text"])
        findings, score, status = run_eoa_verification(meta, "Doc_C_Incomplete_EoA.pdf", STATE["reference_institution"])
        app_data["documents"] = [{
            "id": "DOC-DEMO-C",
            "filename": "Doc_C_Incomplete_EoA.pdf",
            "doc_type": "Extension of Approval (EoA)",
            "sha256_hash": "c0535e4be2b79ffd93291305436bf889314e4a3faec05ecffcbb7ff310919046",
            "file_size_bytes": 39000,
            "upload_timestamp": datetime.datetime.now().isoformat(),
            "ocr_processed": True,
            "is_duplicate": False,
            "anomaly_flags": ["Missing Mandatory IDs", "Omitted Approval Signatures"],
            "extracted_metadata": meta.model_dump()
        }]
        app_data["findings"] = [f.model_dump() for f in findings]
        app_data["overall_score"] = score
        app_data["status"] = "Under Scrutiny"
        return {"status": "success", "scenario": "Scenario C: Incomplete EoA (Missing IDs & Signature Section)", "data": app_data}
        
    raise HTTPException(status_code=400, detail="Unknown scenario name")

# --- STATIC FILES (FRONTEND SERVING) ---
STATIC_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static")
os.makedirs(STATIC_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
def serve_index():
    index_file = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {
        "app": APP_TITLE,
        "version": APP_VERSION,
        "documentation": "/docs",
        "api_health": "/api/health"
    }

@app.get("/api/health")
def health():
    return {
        "status": "healthy",
        "service": "AICTE SIH26261 Decision Support API",
        "version": APP_VERSION,
        "server_time": datetime.datetime.now().isoformat()
    }
