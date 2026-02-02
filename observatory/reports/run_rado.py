"""
RADO — Runtime Authority Drift Observatory (Report Runner)

Read-only, post-hoc observatory over RuntimeStore audit events.

Rules:
- NO mutation
- NO control
- NO evaluation
- NO audit emission
- Descriptive metrics only (non-normative)
"""

from __future__ import annotations

from observatory.authority_drift import AuthorityDriftObservatory


def run_rado(*, store, case_id: str) -> None:
    """
    Execute RADO over a LIVE RuntimeStore instance (injected).

    Important:
    - store is injected by the runtime entrypoint (e.g., run.py)
    - RADO never constructs a store
    - RADO never writes to the store
    """

    events = store.list_audit_events(case_id)

    obs = AuthorityDriftObservatory(events)

    print("\n=== RADO REPORT ===")
    print(f"Case ID: {case_id}")
    print("-------------------\n")

    print("Audit Summary:")
    summary = obs.audit_summary()
    for k, v in summary.items():
        print(f"  {k}: {v}")

    print("\nAuthority Drift Signals:")
    drift = obs.authority_drift_signals()
    for k, v in drift.items():
        print(f"  {k}: {v}")

    print("\nRADO completed (descriptive only).\n")


if __name__ == "__main__":
    print(
        "\nRADO runner is designed to be called with an injected live store.\n"
        "Run it from the runtime entrypoint (run.py), not as a standalone script.\n"
        "Example: python3 run.py\n"
    )