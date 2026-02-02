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

    # ─────────────────────────────────────────────
    # Phase 21B++c — Temporal Authority Drift Windows
    # ─────────────────────────────────────────────

    print("\nTemporal Authority Drift Windows:")
    temporal = obs.temporal_authority_drift_windows()

    print("  Config:")
    for k, v in temporal.get("config", {}).items():
        print(f"    {k}: {v}")

    print("\n  Window Metrics:")
    metrics = temporal.get("metrics", {})
    for k, v in metrics.items():
        print(f"    {k}: {v}")

    print("\n  Windows:")
    windows = temporal.get("windows", [])
    if not windows:
        print("    (no windows)")
    else:
        for i, w in enumerate(windows):
            print(f"    Window {i}:")
            for k, v in w.items():
                print(f"      {k}: {v}")

    episodes = temporal.get("episodes", [])
    print("\n  Drift Episodes:")
    if not episodes:
        print("    (no episodes)")
    else:
        for i, ep in enumerate(episodes):
            print(f"    Episode {i}:")
            for k, v in ep.items():
                print(f"      {k}: {v}")

    print("\nRADO completed (descriptive only).\n")


if __name__ == "__main__":
    print(
        "\nRADO runner is designed to be called with an injected live store.\n"
        "Run it from the runtime entrypoint (run.py), not as a standalone script.\n"
        "Example: python3 run.py\n"
    )
