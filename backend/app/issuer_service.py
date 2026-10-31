import datetime
from typing import Dict, Any
from .models import IssuerVerificationResult
from .seed_data import SIMULATED_ISSUER_REGISTRY

def query_issuer_registry(cert_number: str, submitted_details: Dict[str, Any] = None) -> IssuerVerificationResult:
    """
    Simulates querying an authorized issuing authority registry.
    Explicitly labeled as a prototype simulation.
    """
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    clean_cert = cert_number.strip().upper()
    
    if clean_cert in SIMULATED_ISSUER_REGISTRY:
        reg = SIMULATED_ISSUER_REGISTRY[clean_cert]
        return IssuerVerificationResult(
            cert_number=clean_cert,
            source_name=reg["source_name"],
            submitted_details=submitted_details or {"submitted_cert_no": clean_cert, "subject": reg["subject"]},
            returned_details={
                "authority_type": reg["authority_type"],
                "issued_to": reg["issued_to"],
                "issue_date": reg["issue_date"],
                "valid_till": reg["valid_till"],
                "subject": reg["subject"],
                "registry_status": reg["status"],
                "audit_notes": reg["details"]
            },
            verification_status=reg["status"],
            timestamp=now_str,
            explanation=f"Simulated query against {reg['source_name']}: {reg['details']}",
            is_simulation=True
        )
    else:
        # Default fallback for unlisted certificates in the demo sandbox
        return IssuerVerificationResult(
            cert_number=clean_cert,
            source_name="National Document & Certificate Verification Sandbox (Simulated)",
            submitted_details=submitted_details or {"submitted_cert_no": clean_cert},
            returned_details={
                "search_result": "No matching electronic record in demo mock registry",
                "recommended_channel": "Direct API adapter or manual verification required with issuing authority"
            },
            verification_status="Source Unavailable",
            timestamp=now_str,
            explanation=f"Certificate '{clean_cert}' not located in synthetic mock repository. In production, this would trigger an authorized Digilocker/API gateway handshake.",
            is_simulation=True
        )
