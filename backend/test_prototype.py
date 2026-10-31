import sys
import os

# Add backend to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.main import (
    health, get_applications, run_demo_scenario, 
    verify_certificate_with_issuer, record_officer_action,
    get_audit_log, get_reference_record, get_rules,
    OfficerActionRequest, IssuerQueryRequest
)

def test_full_pipeline_direct():
    print("--- 1. Testing Health Endpoint ---")
    h = health()
    assert h["status"] == "healthy", f"Health failed: {h}"
    print("Health check OK:", h)

    print("\n--- 2. Testing Application Listing ---")
    apps = get_applications()
    assert apps["status"] == "success"
    print(f"Loaded {apps['count']} applications in state.")

    print("\n--- 3. Testing Scenario A (Correct EoA) ---")
    scen_a = run_demo_scenario("scenario_a")
    assert scen_a["status"] == "success"
    app_a = scen_a["data"]
    print(f"Scenario A status: {app_a['status']}, score: {app_a['overall_score']}%")
    assert app_a["overall_score"] >= 80, "Scenario A should have high passing score"

    print("\n--- 4. Testing Scenario B (Intake Mismatch & Missing AI&DS) ---")
    scen_b = run_demo_scenario("scenario_b")
    assert scen_b["status"] == "success"
    app_b = scen_b["data"]
    print(f"Scenario B status: {app_b['status']}, score: {app_b['overall_score']}%")
    assert app_b["status"] == "Correction Required", "Scenario B should require correction"
    mismatch_findings = [f for f in app_b["findings"] if f["status"] in ["Mismatched", "Missing"]]
    print(f"Found {len(mismatch_findings)} mismatch/missing findings in Scenario B:")
    for f in mismatch_findings:
        print(f"  - [{f['status']}] {f['field_name']}: Expected '{f['expected_value']}', Extracted '{f['extracted_value']}'")
    assert len(mismatch_findings) >= 2, "Expected at least 2 findings for Scenario B"

    print("\n--- 5. Testing Scenario C (Incomplete EoA) ---")
    scen_c = run_demo_scenario("scenario_c")
    assert scen_c["status"] == "success"
    app_c = scen_c["data"]
    print(f"Scenario C status: {app_c['status']}, score: {app_c['overall_score']}%")
    assert app_c["status"] in ["Under Scrutiny", "Correction Required"]

    print("\n--- 6. Testing Simulated Issuer Verification Sandbox ---")
    issuer_res = verify_certificate_with_issuer(IssuerQueryRequest(cert_number="CERT-DEMO-101"))
    assert issuer_res["status"] == "success"
    issuer_data = issuer_res["data"]
    print(f"Issuer query for CERT-DEMO-101: {issuer_data['verification_status']} from {issuer_data['source_name']}")
    assert "Verified" in issuer_data["verification_status"]

    print("\n--- 7. Testing Reviewer Action & Audit Trail Recording ---")
    action_req = OfficerActionRequest(
        application_id="APP-2026-001",
        officer_name="Dr. R. K. Sharma",
        officer_role="Scrutiny Officer - Western Regional Office",
        action_type="Correction Requested",
        remarks="Please provide sanctioned AICTE expansion order for Computer Engineering intake increase."
    )
    action_res = record_officer_action(action_req)
    assert action_res["status"] == "success"
    print("Action recorded:", action_res["message"])

    audit_res = get_audit_log()
    assert audit_res["status"] == "success"
    audit_data = audit_res["data"]
    print(f"Audit log now has {len(audit_data)} entries. Latest action: {audit_data[0]['action_type']}")

    print("\n--- 8. Testing Admin Rules & Reference Records ---")
    ref = get_reference_record()
    assert ref["status"] == "success"
    assert ref["data"]["permanent_id"] == "1-1234567890"
    print(f"Reference record verified for: {ref['data']['institution_name']} (PID: {ref['data']['permanent_id']})")

    rules = get_rules()
    assert rules["status"] == "success"
    print(f"Configured rules count: {len(rules['data'])}")

    print("\n========================================================")
    print("ALL 8 VERIFICATION & COMPLIANCE PIPELINE TESTS PASSED!")
    print("========================================================")

if __name__ == "__main__":
    test_full_pipeline_direct()
