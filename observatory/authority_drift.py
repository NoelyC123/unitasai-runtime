"""
Authority Drift Observatory

Read-only.
Descriptive only.
"""

from collections import Counter
from typing import Any

from observatory.stability_recovery import compute_stability_and_recovery
from observatory.temporal_correlation import compute_cross_signal_correlation
from observatory.temporal_windows import TemporalWindowConfig, compute_temporal_windows


class AuthorityDriftObservatory:
    def __init__(self, audit_events):
        self.events = audit_events

    def audit_summary(self):
        actions = [e["action"] for e in self.events]
        counts = Counter(actions)
        return {
            "total_events": len(self.events),
            "actions_breakdown": counts,
            "evaluation_count": counts.get("EVALUATION", 0),
            "intake_count": counts.get("INTAKE", 0),
            "controller_decisions": counts.get("CONTROLLER_DECISION", 0),
            "first_event": self.events[0]["timestamp"] if self.events else None,
            "last_event": self.events[-1]["timestamp"] if self.events else None,
        }

    def authority_drift_signals(self):
        decisions = [e for e in self.events if e["action"] == "CONTROLLER_DECISION"]
        approved = [e for e in decisions if e["payload"]["decision"] == "approved"]
        total = len(decisions)
        return {
            "total_controller_decisions": total,
            "approved_decisions": len(approved),
            "controller_deference_ratio": (len(approved) / total) if total else None,
            "note": "Ratios are descriptive only. No normative interpretation is performed.",
        }

    def temporal_authority_drift_windows(
        self,
        *,
        window_seconds: int = 300,
        drift_threshold: float = 0.25,
    ) -> dict[str, Any]:
        config = TemporalWindowConfig(
            window_seconds=window_seconds,
            drift_threshold=drift_threshold,
        )
        return compute_temporal_windows(self.events, config=config)

    def cross_signal_temporal_correlation(
        self,
        *,
        window_seconds: int = 300,
        drift_threshold: float = 0.25,
        max_lag_windows: int = 3,
    ) -> dict[str, Any]:
        temporal = self.temporal_authority_drift_windows(
            window_seconds=window_seconds,
            drift_threshold=drift_threshold,
        )
        return compute_cross_signal_correlation(
            windows=temporal.get("windows", []),
            max_lag_windows=max_lag_windows,
        )

    # ─────────────────────────────────────────────
    # Phase 21C — Stability & Recovery Metrics
    # ─────────────────────────────────────────────

    def stability_and_recovery_metrics(
        self,
        *,
        window_seconds: int = 300,
        drift_threshold: float = 0.25,
    ) -> dict[str, Any]:
        temporal = self.temporal_authority_drift_windows(
            window_seconds=window_seconds,
            drift_threshold=drift_threshold,
        )
        return compute_stability_and_recovery(
            windows=temporal.get("windows", []),
            episodes=temporal.get("episodes", []),
            drift_threshold=drift_threshold,
        )
