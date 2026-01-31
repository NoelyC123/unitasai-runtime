"""
RADO — Read-only Authority Drift Observatory

This runner performs post-hoc descriptive analysis over audit events.

It:
- Reads audit logs only
- Emits NO audit events
- Performs NO mutation
- Makes NO decisions
- Computes NO enforcement

Purpose:
Describe patterns that may indicate authority drift
under Canon-compliant operation.
"""

from typing import List, Dict
from collections import Counter
from src.storage.runtime_store import RuntimeStore


def summarize_audit_events(events: List[Dict]) -> Dict:
    """
    Produce a structural summary of audit activity.

    This function:
    - Describes frequency and sequencing
    - Does not interpret correctness
    - Does not judge outcomes
    """

    actions = [e["action"] for e in events]

    return {
        "total_events": len(events),
        "actions_breakdown": Counter(actions),
        "evaluation_count": actions.count("EVALUATION"),
        "intake_count": actions.count("INTAKE"),
        "first_event": events[0]["action"] if events else None,
        "last_event": events[-1]["action"] if events else None,
    }


def detect_authority_drift_signals(events: List[Dict]) -> Dict:
    """
    Describe potential authority drift indicators.

    IMPORTANT:
    - This does NOT declare drift
    - This does NOT assess risk severity
    - This does NOT recommend mitigation

    It only surfaces measurable structural signals.
    """

    evaluation_events = [
        e for e in events if e["action"] == "EVALUATION"
    ]

    admissions = 0
    for e in evaluation_events:
        payload = e.get("payload", {})
        if payload.get("admissible") is True:
            admissions += 1

    total = len(evaluation_events)

    return {
        "total_evaluations": total,
        "admitted_evaluations": admissions,
        "admission_ratio": (
            admissions / total if total > 0 else None
        ),
        "note": (
            "Ratios are descriptive only. "
            "No normative interpretation is performed."
        ),
    }


def run_rado(store: RuntimeStore, case_id: str):
    """
    Execute RADO analysis for a single case.

    This function is:
    - Read-only
    - Side-effect free
    """

    events = store.list_audit_events(case_id)

    print("\n=== RADO REPORT ===")
    print(f"Case ID: {case_id}")
    print("-------------------")

    summary = summarize_audit_events(events)
    drift = detect_authority_drift_signals(events)

    print("\nAudit Summary:")
    for k, v in summary.items():
        print(f"  {k}: {v}")

    print("\nAuthority Drift Signals:")
    for k, v in drift.items():
        print(f"  {k}: {v}")

    print("\nRADO completed (descriptive only).")


# ─────────────────────────────────────────────
# CLI entrypoint (manual invocation)
# ─────────────────────────────────────────────

if __name__ == "__main__":
    # NOTE:
    # This runner assumes the runtime store is already populated
    # in-process. For now, we demonstrate structural correctness only.

    store = RuntimeStore()
    run_rado(store=store, case_id="demo-case")