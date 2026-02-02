"""
Authority Drift Observatory

Read-only.
Descriptive only.
"""

from collections import Counter
from typing import Any

from observatory.temporal_windows import TemporalWindowConfig, compute_temporal_windows


class AuthorityDriftObservatory:
    def __init__(self, audit_events):
        self.events = audit_events

    # ─────────────────────────────────────────────
    # Audit summary
    # ─────────────────────────────────────────────

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

    # ─────────────────────────────────────────────
    # Authority drift signals
    # ─────────────────────────────────────────────

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

    # ─────────────────────────────────────────────
    # Phase 21B++c — Temporal Authority Drift Windows
    # ─────────────────────────────────────────────

    def temporal_authority_drift_windows(
        self,
        *,
        window_seconds: int = 300,
        drift_threshold: float = 0.25,
    ) -> dict[str, Any]:
        """
        Compute temporal authority drift windows over existing audit-derived ratios.

        Inputs:
          - Uses self.events (already case-scoped audit events)
          - window_seconds: fixed window size in seconds
          - drift_threshold: absolute L1 delta threshold for episode detection

        Output (descriptive only):
          {
            "config": {...},
            "windows": [...],
            "episodes": [...],
            "metrics": {...}
          }

        Notes:
        - No mutation
        - No authority creation
        - No control or policy inference
        """
        config = TemporalWindowConfig(
            window_seconds=window_seconds,
            drift_threshold=drift_threshold,
        )

        return compute_temporal_windows(
            self.events,
            config=config,
        )
