"""
Synthetic Seed Data for SIH26261 Demonstration Prototype
All data is strictly fictional and generated for prototype demonstration purposes.
"""

from typing import Dict, Any, List

SYNTHETIC_REFERENCE_INSTITUTION = {
    "institution_name": "ABC Institute of Technology",
    "permanent_id": "1-1234567890",
    "application_id": "APP-DEMO-001",
    "academic_year": "2026-27",
    "address": "Sector 24, Pradhikaran, Nigdi, Pune, Maharashtra - 411044",
    "affiliating_university": "Savitribai Phule Pune University",
    "approval_status": "Approved",
    "issue_date": "15/06/2026",
    "programmes": ["ENGINEERING AND TECHNOLOGY"],
    "courses": [
        {
            "programme": "ENGINEERING AND TECHNOLOGY",
            "level": "UG",
            "course_name": "COMPUTER ENGINEERING",
            "affiliating_body": "Savitribai Phule Pune University",
            "approved_intake": 120
        },
        {
            "programme": "ENGINEERING AND TECHNOLOGY",
            "level": "UG",
            "course_name": "ARTIFICIAL INTELLIGENCE AND DATA SCIENCE",
            "affiliating_body": "Savitribai Phule Pune University",
            "approved_intake": 60
        }
    ],
    "is_synthetic": True
}

# Regulatory Rules configured by AICTE Admin
DEFAULT_COMPLIANCE_RULES = [
    {
        "rule_id": "RULE-INST-001",
        "rule_name": "Permanent Institute ID Verification",
        "category": "Institutional Identity",
        "description": "Verifies that the Permanent Institute ID extracted from the submitted approval document matches the institutional reference record.",
        "condition_type": "Exact_Match",
        "is_active": True,
        "is_prototype": True
    },
    {
        "rule_id": "RULE-INST-002",
        "rule_name": "Application ID Alignment",
        "category": "Institutional Identity",
        "description": "Ensures the Application ID on all uploaded documents corresponds to the currently scrutinized application cycle.",
        "condition_type": "Exact_Match",
        "is_active": True,
        "is_prototype": True
    },
    {
        "rule_id": "RULE-INST-003",
        "rule_name": "Academic Session Consistency",
        "category": "Regulatory Period",
        "description": "Validates that the approval extension is specifically sought for the authorized academic year (2026-27).",
        "condition_type": "Exact_Match",
        "is_active": True,
        "is_prototype": True
    },
    {
        "rule_id": "RULE-CRS-001",
        "rule_name": "Approved Course Name & Intake Quota Verification",
        "category": "Curriculum & Intake",
        "description": "Validates that each extracted course exists in the authorized catalogue and student intake capacity does not exceed authorized limits.",
        "condition_type": "Catalogue_and_Limit_Check",
        "is_active": True,
        "is_prototype": True
    },
    {
        "rule_id": "RULE-CRS-002",
        "rule_name": "Mandatory Course Catalogue Completeness",
        "category": "Curriculum & Intake",
        "description": "Checks if all approved courses (including newly sanctioned AI & Data Science) are documented without omissions.",
        "condition_type": "Completeness_Check",
        "is_active": True,
        "is_prototype": True
    },
    {
        "rule_id": "RULE-SEC-001",
        "rule_name": "Document Duplicate & SHA-256 Tamper Detection",
        "category": "Security & Integrity",
        "description": "Calculates cryptographic SHA-256 checksums to detect duplicate uploads across institutions and flag digital tampering.",
        "condition_type": "Cryptographic_Integrity",
        "is_active": True,
        "is_prototype": True
    },
    {
        "rule_id": "RULE-AUTH-001",
        "rule_name": "Issuing Authority Digital Signature Completeness",
        "category": "Document Authentication",
        "description": "Validates that the document contains a complete digital authorization block or signature placeholder.",
        "condition_type": "Signature_Block_Check",
        "is_active": True,
        "is_prototype": True
    },
    {
        "rule_id": "RULE-NOC-001",
        "rule_name": "Mandatory Statutory NOC & Validity Period",
        "category": "Statutory Compliance",
        "description": "Confirms presence of Fire Safety NOC and verifies the expiration date is within current academic cycle.",
        "condition_type": "Validity_Date_Check",
        "is_active": True,
        "is_prototype": True
    }
]

# Simulated External Issuing Authorities Database (Mock Registry)
SIMULATED_ISSUER_REGISTRY = {
    "CERT-DEMO-101": {
        "cert_number": "CERT-DEMO-101",
        "source_name": "Maharashtra State Fire Services Directorate",
        "authority_type": "State Statutory Authority",
        "issued_to": "ABC Institute of Technology, Pune",
        "subject": "Fire Safety Compliance & NOC for Educational Building",
        "issue_date": "10/01/2026",
        "valid_till": "09/01/2027",
        "status": "Verified in Demo Sandbox",
        "details": "Structure complies with National Building Code (NBC) Part IV norms. Inspection conducted on 05/01/2026.",
        "is_valid": True
    },
    "CERT-DEMO-102": {
        "cert_number": "CERT-DEMO-102",
        "source_name": "Pune Municipal Corporation (Town Planning Division)",
        "authority_type": "Municipal Local Body",
        "issued_to": "ABC Institute of Technology, Pune",
        "subject": "Sanctioned Building Completion Certificate",
        "issue_date": "05/03/2024",
        "valid_till": "Lifetime (Permanent)",
        "status": "Verified in Demo Sandbox",
        "details": "Educational campus building completion approved for Survey No. 45/2.",
        "is_valid": True
    },
    "CERT-DEMO-EXPIRED": {
        "cert_number": "CERT-DEMO-EXPIRED",
        "source_name": "Maharashtra Pollution Control Board (MPCB)",
        "authority_type": "Environmental Board",
        "issued_to": "ABC Institute of Technology, Pune",
        "subject": "Consent to Operate (Water & Air)",
        "issue_date": "01/01/2023",
        "valid_till": "31/12/2025",
        "status": "Expired",
        "details": "Consent expired on 31/12/2025. Renewal application pending with regional office.",
        "is_valid": False
    },
    "CERT-DEMO-TAMPERED": {
        "cert_number": "CERT-DEMO-TAMPERED",
        "source_name": "Land Records Revenue Department",
        "authority_type": "State Revenue Department",
        "issued_to": "Unknown Entity (Altered Record)",
        "subject": "Land Title Ownership & Non-Agricultural Certificate",
        "issue_date": "12/04/2020",
        "valid_till": "Permanent",
        "status": "Mismatch Detected",
        "details": "Submitted survey number 128-B does not match issuer registered parcel 128-A.",
        "is_valid": False
    }
}

# Infrastructure Checklist Items for AICTE Inspection
DEFAULT_INFRASTRUCTURE_ITEMS = [
    {
        "id": "INFRA-001",
        "category": "Laboratories",
        "title": "Artificial Intelligence & Data Science Specialist Lab",
        "required_specs": "Minimum 66 sq.m area, 35 high-end GPU workstations (16GB RAM, RTX 4060), 100 Mbps LAN connectivity, UPS backup.",
        "submitted_photos": [
            "/demo-images/lab_ai_1.jpg",
            "/demo-images/lab_ai_2.jpg"
        ],
        "submitted_documents": ["Lab_Stock_Register_Extract.pdf"],
        "status": "Compliant",
        "officer_remark": "Laboratory photos and equipment invoices reviewed. Hardware configuration meets AICTE emerging technologies norms.",
        "last_inspected": "2026-06-18"
    },
    {
        "id": "INFRA-002",
        "category": "Laboratories",
        "title": "Computer Networks & Operating Systems Lab",
        "required_specs": "Minimum 66 sq.m area, 30 desktop terminals, Cisco managed switches, structured cabling.",
        "submitted_photos": [
            "/demo-images/lab_nw_1.jpg"
        ],
        "submitted_documents": ["Hardware_AMC_Certificate.pdf"],
        "status": "Compliant",
        "officer_remark": "Adequate workstation capacity and licensed simulation tools demonstrated.",
        "last_inspected": "2026-06-18"
    },
    {
        "id": "INFRA-003",
        "category": "Classrooms",
        "title": "Smart Classrooms (Division A & B)",
        "required_specs": "Minimum 66 sq.m carpet area each, ceiling-mounted interactive smart display/projector, Wi-Fi 6 coverage, ergonomic seating.",
        "submitted_photos": [
            "/demo-images/classroom_1.jpg"
        ],
        "submitted_documents": ["Classroom_Layout_Plan.pdf"],
        "status": "Compliant",
        "officer_remark": "Both division classrooms meet ventilation and natural lighting standards.",
        "last_inspected": "2026-06-18"
    },
    {
        "id": "INFRA-004",
        "category": "Central Library",
        "title": "Digital Library & Learning Resource Center",
        "required_specs": "Minimum 400 sq.m area, 25,000+ technical volumes, 50 IEEE/ACM international journals, 20 digital terminals.",
        "submitted_photos": [
            "/demo-images/library_1.jpg"
        ],
        "submitted_documents": ["Book_Purchase_Invoices_AY2026.pdf"],
        "status": "Pending Review",
        "officer_remark": "Digital terminal count meets minimum 20 nodes; e-journal subscription receipt for 2026 under audit verification.",
        "last_inspected": "2026-06-19"
    },
    {
        "id": "INFRA-005",
        "category": "Barrier-Free Environment",
        "title": "Differently-Abled Accessibility Features",
        "required_specs": "Anti-skid access ramps with gradient <= 1:12, braille signage, dedicated accessible washroom per floor, operational elevator.",
        "submitted_photos": [
            "/demo-images/ramp_access.jpg"
        ],
        "submitted_documents": ["Accessibility_Architect_Certificate.pdf"],
        "status": "Refer for Inspection",
        "officer_remark": "Ramp photos provided for Ground Floor only; physical expert committee inspection recommended to verify upper-floor lift access.",
        "last_inspected": "2026-06-20"
    }
]

# Sample Applications Pre-populated for Instant Demonstrations
INITIAL_APPLICATIONS = [
    {
        "id": "APP-2026-001",
        "application_id": "APP-DEMO-001",
        "institution_id": "INST-PUNE-01",
        "institution_name": "ABC Institute of Technology",
        "permanent_id": "1-1234567890",
        "academic_year": "2026-27",
        "category": "Extension of Approval (EoA)",
        "status": "Preliminary Checks Completed",
        "created_at": "2026-06-16T10:30:00Z",
        "submitted_at": "2026-06-16T11:15:00Z",
        "documents": [
            {
                "id": "DOC-001",
                "filename": "Doc_A_Correct_EoA.pdf",
                "doc_type": "Extension of Approval (EoA)",
                "sha256_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
                "file_size_bytes": 48200,
                "upload_timestamp": "2026-06-16T11:10:00Z",
                "ocr_processed": True,
                "is_duplicate": False,
                "anomaly_flags": []
            },
            {
                "id": "DOC-002",
                "filename": "Fire_Safety_Certificate_CERT-DEMO-101.pdf",
                "doc_type": "Fire Safety NOC",
                "sha256_hash": "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e",
                "file_size_bytes": 35400,
                "upload_timestamp": "2026-06-16T11:12:00Z",
                "ocr_processed": True,
                "is_duplicate": False,
                "anomaly_flags": []
            }
        ],
        "findings": [],
        "infrastructure_items": DEFAULT_INFRASTRUCTURE_ITEMS,
        "reviewer_actions": [
            {
                "action_id": "ACT-001",
                "application_id": "APP-2026-001",
                "officer_name": "Dr. R. K. Sharma",
                "officer_role": "Scrutiny Officer - Western Regional Office",
                "action_type": "Observation Added",
                "remarks": "Preliminary AI-assisted validation shows complete alignment with sanctioned institutional records. Recommend clearance of technical intake.",
                "timestamp": "2026-06-18T14:22:00Z",
                "related_finding_id": None
            }
        ],
        "overall_score": 96.5
    },
    {
        "id": "APP-2026-002",
        "application_id": "APP-DEMO-002",
        "institution_id": "INST-PUNE-02",
        "institution_name": "Modern Technical Campus",
        "permanent_id": "1-9876543210",
        "academic_year": "2026-27",
        "category": "Extension of Approval (EoA)",
        "status": "Correction Required",
        "created_at": "2026-06-15T09:00:00Z",
        "submitted_at": "2026-06-15T10:00:00Z",
        "documents": [
            {
                "id": "DOC-003",
                "filename": "Doc_B_Incorrect_EoA.pdf",
                "doc_type": "Extension of Approval (EoA)",
                "sha256_hash": "7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069",
                "file_size_bytes": 45100,
                "upload_timestamp": "2026-06-15T09:55:00Z",
                "ocr_processed": True,
                "is_duplicate": False,
                "anomaly_flags": ["Intake Discrepancy", "Course Omission"]
            }
        ],
        "findings": [
            {
                "finding_id": "FND-MISMATCH-01",
                "rule_name": "Approved Course Name & Intake Quota Verification",
                "field_name": "Computer Engineering Intake",
                "expected_value": 120,
                "extracted_value": 180,
                "status": "Mismatched",
                "severity": "Critical",
                "document_ref": "Doc_B_Incorrect_EoA.pdf",
                "page_ref": 1,
                "explanation": "Extracted intake of 180 seats exceeds the institutional reference sanctioned limit of 120 seats without required AICTE Expansion sanction.",
                "recommended_action": "Issue formal discrepancy notice and request institutional reconciliation."
            },
            {
                "finding_id": "FND-MISSING-01",
                "rule_name": "Mandatory Course Catalogue Completeness",
                "field_name": "Course: Artificial Intelligence & Data Science",
                "expected_value": "AI & DS (60 Seats)",
                "extracted_value": "NOT FOUND",
                "status": "Missing",
                "severity": "Warning",
                "document_ref": "Doc_B_Incorrect_EoA.pdf",
                "page_ref": 1,
                "explanation": "Authorized course 'Artificial Intelligence and Data Science' with 60 sanctioned intake was omitted from the submitted document table.",
                "recommended_action": "Request revised EoA schedule reflecting complete academic offerings."
            }
        ],
        "infrastructure_items": [],
        "reviewer_actions": [
            {
                "action_id": "ACT-002",
                "application_id": "APP-2026-002",
                "officer_name": "Prof. S. N. Patil",
                "officer_role": "Regional Scrutiny Officer",
                "action_type": "Correction Requested",
                "remarks": "Major mismatch in Computer Engineering student intake (submitted 180 vs sanctioned 120) and missing AI&DS programme. College notified for clarification.",
                "timestamp": "2026-06-17T11:05:00Z",
                "related_finding_id": "FND-MISMATCH-01"
            }
        ],
        "overall_score": 42.0
    },
    {
        "id": "APP-2026-003",
        "application_id": "APP-DEMO-003",
        "institution_id": "INST-PUNE-03",
        "institution_name": "Pune Vidya College of Engineering",
        "permanent_id": "1-5544332211",
        "academic_year": "2026-27",
        "category": "Extension of Approval (EoA)",
        "status": "Under Scrutiny",
        "created_at": "2026-06-19T14:10:00Z",
        "submitted_at": "2026-06-19T16:00:00Z",
        "documents": [
            {
                "id": "DOC-004",
                "filename": "Doc_C_Incomplete_EoA.pdf",
                "doc_type": "Extension of Approval (EoA)",
                "sha256_hash": "c0535e4be2b79ffd93291305436bf889314e4a3faec05ecffcbb7ff310919046",
                "file_size_bytes": 39000,
                "upload_timestamp": "2026-06-19T15:45:00Z",
                "ocr_processed": True,
                "is_duplicate": False,
                "anomaly_flags": ["Missing Identifiers", "Incomplete Signatures"]
            }
        ],
        "findings": [
            {
                "finding_id": "FND-INCOMP-01",
                "rule_name": "Permanent Institute ID Verification",
                "field_name": "Permanent Institute ID",
                "expected_value": "1-1234567890",
                "extracted_value": "[NOT PROVIDED / UNREADABLE]",
                "status": "Missing",
                "severity": "Critical",
                "document_ref": "Doc_C_Incomplete_EoA.pdf",
                "page_ref": 1,
                "explanation": "Mandatory Institutional identifier field is blank or omitted.",
                "recommended_action": "Reject incomplete submission; require full digitally signed copy."
            },
            {
                "finding_id": "FND-INCOMP-02",
                "rule_name": "Issuing Authority Digital Signature Completeness",
                "field_name": "Approval Authority Digital Signature",
                "expected_value": "Member Secretary Signature Block",
                "extracted_value": "MISSING",
                "status": "Manual Review Required",
                "severity": "Critical",
                "document_ref": "Doc_C_Incomplete_EoA.pdf",
                "page_ref": 1,
                "explanation": "Statutory signatory block not identified. Document cannot be validated automatically.",
                "recommended_action": "Refer to Standing Hearing Committee (SHC) or request certified copy."
            }
        ],
        "infrastructure_items": [],
        "reviewer_actions": [],
        "overall_score": 25.0
    }
]

# Supported Application Categories
SUPPORTED_CATEGORIES = [
    {
        "category_id": "CAT-EOA",
        "name": "Extension of Approval (EoA)",
        "code": "EOA",
        "description": "Annual renewal and validation of sanctioned intake, courses, and statutory compliance for continuing institutions.",
        "mandatory_documents": [
            "Previous Year EoA Document",
            "Fire Safety NOC Certificate",
            "Building Completion Certificate",
            "Faculty Cadre Roster & Qualifications",
            "Anti-Ragging Committee Constitution"
        ],
        "is_active": True,
        "is_primary_demo": True
    },
    {
        "category_id": "CAT-NEW",
        "name": "Grant of New Technical Institution Approval",
        "code": "NEW_INST",
        "description": "Comprehensive appraisal of newly proposed polytechnic, engineering, management, or pharmacy colleges.",
        "mandatory_documents": [
            "Registered Land Title / Deed",
            "Approved Building Master Plan",
            "Fixed Deposit Receipt (FDR) / Corpus Fund",
            "AICTE Inspection Expert Committee Report"
        ],
        "is_active": False,
        "is_primary_demo": False
    },
    {
        "category_id": "CAT-INTAKE",
        "name": "Increase in Intake / Introduction of New Course",
        "code": "INTAKE_EXP",
        "description": "Application for enhancing student intake capacity or establishing emerging technical specializations.",
        "mandatory_documents": [
            "NBA / NAAC Accreditation Certificate",
            "Additional Built-up Area Architectural Certificate",
            "Faculty Availability Roster"
        ],
        "is_active": False,
        "is_primary_demo": False
    }
]
