"""
RADO — Runtime Authority Drift Observatory (Report Runner)

Read-only, post-hoc observatory over RuntimeStore audit events.
"""

from __future__ import annotations

from observatory.authority_drift import AuthorityDriftObservatory
from observatory.presentation.temporal_windows_text import (
    format_drift_episodes,
    format_temporal_summary,
    format_window_table,
    join_blocks,
)


def run_rado(*, store, case_id: str) -> None:
    events = store.list_audit_events(case_id)
    obs = AuthorityDriftObservatory(events)

    print("\n=== RADO REPORT ===")
    print(f"Case ID: {case_id}\n")

    print("Audit Summary:")
    for k, v in obs.audit_summary().items():
        print(f"  {k}: {v}")

    print("\nAuthority Drift Signals:")
    for k, v in obs.authority_drift_signals().items():
        print(f"  {k}: {v}")

    temporal = obs.temporal_authority_drift_windows()

    print("\nTemporal Authority Drift:")
    print(
        join_blocks(
            format_temporal_summary(temporal),
            format_drift_episodes(temporal),
            format_window_table(temporal),
        )
    )

    corr = obs.cross_signal_temporal_correlation()
    print("\nCross-Signal Temporal Correlation:")
    print(f"  Zero-lag r: {corr['zero_lag']['pearson_r']}")

    stability = obs.stability_and_recovery_metrics()
    print("\nStability & Recovery Metrics:")
    for k, v in stability.items():
        print(f"  {k}: {v}")

    health = obs.epistemic_health_index()
    print("\nEpistemic Health Index:")
    for section, values in health.items():
        print(f"  {section}:")
        if isinstance(values, dict):
            for k, v in values.items():
                print(f"    {k}: {v}")
        else:
            print(f"    {values}")

    print("\nRADO completed (descriptive only).\n")
