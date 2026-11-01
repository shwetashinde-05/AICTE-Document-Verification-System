"""
Regulatory Reference and Benchmark Configuration Data
Maintains AICTE institutional benchmark records, compliance rules, and statutory categories.
"""

from typing import Dict, Any, List

SYNTHETIC_REFERENCE_INSTITUTION = {
    "institution_name": "ABC Institute of Technology",
    "permanent_id": "1-1234567890",
    "application_id": "APP-2026-001",
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
    "is_synthetic": False
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
        "is_prototype": False
    },
    {
        "rule_id": "RULE-INST-002",
        "rule_name": "Application ID Alignment",
        "category": "Institutional Identity",
        "description": "Ensures the Application ID on all uploaded documents corresponds to the currently scrutinized application cycle.",
        "condition_type": "Exact_Match",
        "is_active": True,
        "is_prototype": False
    },
    {
        "rule_id": "RULE-INST-003",
        "rule_name": "Academic Session Consistency",
        "category": "Regulatory Period",
        "description": "Validates that the approval extension is specifically sought for the authorized academic year (2026-27).",
        "condition_type": "Exact_Match",
        "is_active": True,
        "is_prototype": False
    },
    {
        "rule_id": "RULE-CRS-001",
        "rule_name": "Approved Course Name & Intake Quota Verification",
        "category": "Curriculum & Intake",
        "description": "Validates that each extracted course exists in the authorized catalogue and student intake capacity does not exceed authorized limits.",
        "condition_type": "Catalogue_and_Limit_Check",
        "is_active": True,
        "is_prototype": False
    },
    {
        "rule_id": "RULE-CRS-002",
        "rule_name": "Mandatory Course Catalogue Completeness",
        "category": "Curriculum & Intake",
        "description": "Checks if all approved courses (including newly sanctioned AI & Data Science) are documented without omissions.",
        "condition_type": "Completeness_Check",
        "is_active": True,
        "is_prototype": False
    },
    {
        "rule_id": "RULE-SEC-001",
        "rule_name": "Document Duplicate & SHA-256 Tamper Detection",
        "category": "Security & Integrity",
        "description": "Calculates cryptographic SHA-256 checksums to detect duplicate uploads across institutions and flag digital tampering.",
        "condition_type": "Cryptographic_Integrity",
        "is_active": True,
        "is_prototype": False
    },
    {
        "rule_id": "RULE-AUTH-001",
        "rule_name": "Issuing Authority Digital Signature Completeness",
        "category": "Document Authentication",
        "description": "Validates that the document contains a complete digital authorization block or signature placeholder.",
        "condition_type": "Signature_Block_Check",
        "is_active": True,
        "is_prototype": False
    },
    {
        "rule_id": "RULE-NOC-001",
        "rule_name": "Mandatory Statutory NOC & Validity Period",
        "category": "Statutory Compliance",
        "description": "Confirms presence of Fire Safety NOC and verifies the expiration date is within current academic cycle.",
        "condition_type": "Validity_Date_Check",
        "is_active": True,
        "is_prototype": False
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
        "status": "Verified in Authority Registry",
        "details": "Structure complies with National Building Code (NBC) Part IV norms. Inspection conducted on 05/01/2026.",
        "is_valid": True
    },
    "MSFS-NOC-2026-101": {
        "cert_number": "MSFS-NOC-2026-101",
        "source_name": "Maharashtra State Fire Services Directorate",
        "authority_type": "State Statutory Authority",
        "issued_to": "ABC Institute of Technology, Pune",
        "subject": "Fire Safety Compliance & NOC for Educational Building",
        "issue_date": "10/01/2026",
        "valid_till": "09/01/2027",
        "status": "Verified in Authority Registry",
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
        "status": "Verified in Authority Registry",
        "details": "Educational campus building completion approved for Survey No. 45/2.",
        "is_valid": True
    },
    "PMC-BCC-2024-102": {
        "cert_number": "PMC-BCC-2024-102",
        "source_name": "Pune Municipal Corporation (Town Planning Division)",
        "authority_type": "Municipal Local Body",
        "issued_to": "ABC Institute of Technology, Pune",
        "subject": "Sanctioned Building Completion Certificate",
        "issue_date": "05/03/2024",
        "valid_till": "Lifetime (Permanent)",
        "status": "Verified in Authority Registry",
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

# Initial Application Repository (Clean state for live submission)
INITIAL_APPLICATIONS: List[Dict[str, Any]] = []

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
        "is_active": True
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
        "is_active": True
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
        "is_active": True
    }
]
