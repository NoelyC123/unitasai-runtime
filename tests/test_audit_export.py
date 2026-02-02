from observatory.audit_export import build_audit_export_bundle


def test_governance_audit_export_bundle_shape():
    out = build_audit_export_bundle(
        case_id="case_001",
        temporal={"windows": []},
        stability={"stability_index": None},
        health={"note": "ok"},
    )
    assert out["case_id"] == "case_001"
    assert "temporal_authority_drift" in out
    assert "stability_and_recovery" in out
    assert "epistemic_health_index" in out
