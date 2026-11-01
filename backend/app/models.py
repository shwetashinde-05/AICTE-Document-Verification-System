from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

class User(BaseModel):
    username: str
    role: str  # 'institution', 'aicte_admin', 'aicte_officer'
    name: str
    organization: str
    institution_id: Optional[str] = None
    email: str

class CourseIntake(BaseModel):
    programme: str
    level: str
    course_name: str
    affiliating_body: str
    approved_intake: int

class InstitutionalReference(BaseModel):
    institution_name: str
    permanent_id: str
    application_id: str
    academic_year: str
    address: str
    affiliating_university: str
    approval_status: str
    issue_date: str
    courses: List[CourseIntake]
    is_synthetic: bool = True

class ExtractedMetadata(BaseModel):
    institution_name: Optional[str] = None
    permanent_id: Optional[str] = None
    application_id: Optional[str] = None
    academic_year: Optional[str] = None
    approval_status: Optional[str] = None
    issue_date: Optional[str] = None
    courses: List[CourseIntake] = []
    cert_numbers: List[str] = []
    raw_text_length: int = 0
    confidence_score: float = 0.95
    has_signature_block: bool = False
    extraction_method: str = "PyMuPDF_Tesseract_Hybrid"
    page_count: int = 1

class DocumentRecord(BaseModel):
    id: str
    filename: str
    doc_type: str  # 'EoA_Document', 'Fire_Safety_NOC', 'Building_Plan', 'Land_Document', 'Faculty_List'
    sha256_hash: str
    file_size_bytes: int
    upload_timestamp: str
    extracted_metadata: Optional[ExtractedMetadata] = None
    ocr_processed: bool = False
    is_duplicate: bool = False
    anomaly_flags: List[str] = []

class VerificationFinding(BaseModel):
    finding_id: str
    rule_name: str
    field_name: str
    expected_value: Any
    extracted_value: Any
    status: str  # 'Matched', 'Mismatched', 'Missing', 'Expired', 'Manual Review Required', 'Pending'
    severity: str  # 'Pass', 'Warning', 'Critical'
    document_ref: str
    page_ref: int = 1
    explanation: str
    recommended_action: str

class IssuerVerificationResult(BaseModel):
    cert_number: str
    source_name: str
    submitted_details: Dict[str, Any]
    returned_details: Dict[str, Any]
    verification_status: str  # 'Verified in Demo Sandbox', 'Mismatch Detected', 'Expired', 'Source Unavailable'
    timestamp: str
    explanation: str
    is_simulation: bool = True

class InfrastructureItem(BaseModel):
    id: str
    category: str  # 'Laboratories', 'Classrooms', 'Library', 'Computer Center', 'Building'
    title: str
    required_specs: str
    submitted_photos: List[str] = []
    submitted_documents: List[str] = []
    status: str  # 'Compliant', 'Deficiency Found', 'Pending Review', 'Refer for Inspection'
    officer_remark: Optional[str] = None
    last_inspected: Optional[str] = None

class ReviewerAction(BaseModel):
    action_id: str
    application_id: str
    officer_name: str
    officer_role: str
    action_type: str  # 'Observation Added', 'Correction Requested', 'Refer for Physical Inspection', 'Escalated', 'Approved for Scrutiny'
    remarks: str
    timestamp: str
    related_finding_id: Optional[str] = None

class ComplianceRule(BaseModel):
    rule_id: str
    rule_name: str
    category: str
    description: str
    condition_type: str
    is_active: bool = True
    is_prototype: bool = True

class Application(BaseModel):
    id: str
    application_id: str
    institution_id: str
    institution_name: str
    permanent_id: str
    academic_year: str
    category: str  # 'Extension of Approval (EoA)'
    status: str  # 'Draft', 'Submitted', 'Preliminary Checks Completed', 'Correction Required', 'Under Scrutiny', 'Inspection Recommended'
    created_at: str
    submitted_at: Optional[str] = None
    documents: List[DocumentRecord] = []
    findings: List[VerificationFinding] = []
    infrastructure_items: List[InfrastructureItem] = []
    issuer_checks: List[IssuerVerificationResult] = []
    reviewer_actions: List[ReviewerAction] = []
    overall_score: float = 0.0
