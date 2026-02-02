"""
Authority Drift Observatory

Read-only.
Descriptive only.
"""

from collections import Counter


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
        decisions = [
            e for e in self.events
            if e["action"] == "CONTROLLER_DECISION"
        ]

        approved = [
            e for e in decisions
            if e["payload"]["decision"] == "approved"
        ]

        total = len(decisions)

        return {
            "total_controller_decisions": total,
            "approved_decisions": len(approved),
            "controller_deference_ratio":
                (len(approved) / total) if total else None,
            "note":
                "Ratios are descriptive only. No normative interpretation is performed.",
        }