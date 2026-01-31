"""
Phase 21B — Evaluation Engine (Refined)

This engine evaluates belief candidates against invariants.

It:
- produces read-only evaluation artifacts
- respects belief scope
- applies invariant strength deterministically

It does NOT:
- mutate beliefs
- decide outcomes
- trigger revision
- resolve tensions
"""

from typing import List, Dict
from src.evaluation.evaluation_types import EvaluationResult


class EvaluationEngine:
    """
    Deterministic evaluation engine.

    Given:
    - a belief candidate
    - a set of invariants

    Produces:
    - an EvaluationResult artifact
    """

    def __init__(self, invariants: List[Dict]):
        self.invariants = invariants

    def evaluate(self, belief: Dict, case_id: str) -> EvaluationResult:
        """
        Evaluate a single belief candidate against all active invariants.
        """

        hard_violations: List[str] = []
        soft_conflicts: List[str] = []

        for invariant in self.invariants:
            if invariant.get("status") != "active":
                continue

            violated = self._check_violation(invariant, belief)

            if not violated:
                continue

            if invariant.get("strength") == "hard":
                hard_violations.append(invariant["id"])
            else:
                soft_conflicts.append(invariant["id"])

        return EvaluationResult.create(
            belief_id=belief["id"],
            case_id=case_id,
            scope=belief["scope"],
            hard_violations=hard_violations,
            soft_conflicts=soft_conflicts,
        )

    def _check_violation(self, invariant: Dict, belief: Dict) -> bool:
        """
        Placeholder invariant predicate evaluation.

        Canon v0.1:
        - Invariant grammar is intentionally underspecified
        - This method MUST remain conservative
        - No inference, no interpretation
        """

        # Explicitly non-operational in v0.1
        return False