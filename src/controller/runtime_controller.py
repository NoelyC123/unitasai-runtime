"""
Runtime Controller

Explicit authority boundary.
No inference.
All decisions are auditable.
"""

import uuid


class RuntimeController:
    def __init__(self, *, store):
        self.store = store

    # ─────────────────────────────────────────────
    # Identity
    # ─────────────────────────────────────────────

    def new_belief_id(self) -> str:
        return str(uuid.uuid4())

    # ─────────────────────────────────────────────
    # Authorisation (Phase 1–3)
    # ─────────────────────────────────────────────

    def authorise_intake(self, case_id: str, raw_query: str) -> bool:
        # Canon v0.1: intake always permitted
        return True

    # ─────────────────────────────────────────────
    # Evaluation decision (EXPLICIT)
    # ─────────────────────────────────────────────

    def decide_evaluation(self, *, case_id: str, evaluation: dict) -> bool:
        """
        Explicit controller decision.

        Decision is audit-visible.
        No inference.
        """
        decision = evaluation["is_admissible"]

        self.store.log(
            case_id=case_id,
            action="CONTROLLER_DECISION",
            payload={
                "belief_id": evaluation["belief_id"],
                "decision": "approved" if decision else "blocked",
                "scope": evaluation["scope"],
            },
        )

        return decision

    # ─────────────────────────────────────────────
    # Audit helpers
    # ─────────────────────────────────────────────

    def audit_intake(self, case_id: str, raw_query: str, beliefs: list):
        self.store.log(
            case_id=case_id,
            action="INTAKE",
            payload={
                "raw_query": raw_query,
                "belief_ids": [b["id"] for b in beliefs],
            },
        )
