"""
Runtime Controller

The ONLY authority-bearing component in the runtime system.

Responsibilities:
- authorise epistemic actions
- mediate between subsystems
- emit audit events
- NEVER infer truth
- NEVER resolve disagreement
"""

import uuid
import time
from typing import List, Dict

from src.evaluation.evaluation_engine import EvaluationEngine


class RuntimeController:
    """
    Central epistemic authority.

    Engines:
    - generate (hypotheses)
    - evaluate (read-only checks)

    Controllers:
    - authorise
    - sequence
    - audit

    This class MUST remain conservative.
    """

    # ─────────────────────────────────────────────
    # Intake authorisation (Phase 23)
    # ─────────────────────────────────────────────

    def authorise_intake(self, case_id: str, raw_query: str) -> bool:
        """
        Determine whether intake is permitted.

        Phase 23:
        - Always true
        - Reserved for future policy enforcement
        """
        return True

    # ─────────────────────────────────────────────
    # Identity helpers
    # ─────────────────────────────────────────────

    def new_belief_id(self) -> str:
        """
        Generate a globally unique belief identifier.
        """
        return str(uuid.uuid4())

    # ─────────────────────────────────────────────
    # Audit helpers
    # ─────────────────────────────────────────────

    def audit_intake(self, case_id: str, raw_query: str, beliefs: List[Dict]):
        """
        Record intake event (Phase 23).
        """
        print(
            f"[AUDIT] {time.time()} — Intake for case {case_id}: "
            f"{len(beliefs)} candidate beliefs"
        )

    def audit_evaluation(self, case_id: str, evaluations):
        """
        Record evaluation event (Phase 21B).
        """
        print(
            f"[AUDIT] {time.time()} — Evaluation for case {case_id}: "
            f"{len(evaluations)} evaluation artifacts"
        )

    # ─────────────────────────────────────────────
    # Phase 21B — Evaluation wiring (READ-ONLY)
    # ─────────────────────────────────────────────

    def evaluate_beliefs(
        self,
        case_id: str,
        beliefs: List[Dict],
        invariants: List[Dict],
    ):
        """
        Phase 21B — Evaluate belief candidates against invariants.

        IMPORTANT:
        - No mutation
        - No decisions
        - No filtering
        - No revision
        """

        engine = EvaluationEngine(invariants)
        results = []

        for belief in beliefs:
            result = engine.evaluate(belief, case_id)
            results.append(result)

        self.audit_evaluation(case_id, results)

        return results