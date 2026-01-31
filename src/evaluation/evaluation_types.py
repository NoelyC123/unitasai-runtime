"""
Phase 21B — Evaluation Types (Refined)

Evaluation artifacts are:
- deterministic
- immutable
- read-only
- non-authoritative

They DESCRIBE epistemic constraint interaction.
They DO NOT decide outcomes.
They DO NOT recommend action.
"""

from dataclasses import dataclass
from typing import List
import time
import uuid


@dataclass(frozen=True)
class EvaluationResult:
    """
    Immutable evaluation artifact.

    This object records how a belief candidate
    interacts with invariants under its declared scope.

    It does NOT:
    - approve beliefs
    - reject beliefs
    - trigger revision
    - mutate state
    """

    evaluation_id: str
    belief_id: str
    case_id: str

    scope: str  # assertive | counterfactual | meta

    admissible: bool
    hard_violations: List[str]
    soft_conflicts: List[str]

    timestamp: float

    @staticmethod
    def create(
        belief_id: str,
        case_id: str,
        scope: str,
        hard_violations: List[str],
        soft_conflicts: List[str],
    ) -> "EvaluationResult":
        """
        Deterministic factory.

        Admissibility rules:
        - Assertive beliefs are inadmissible if hard violations exist
        - Counterfactual beliefs remain admissible but are flagged
        """

        admissible = True

        if scope == "assertive" and hard_violations:
            admissible = False

        return EvaluationResult(
            evaluation_id=str(uuid.uuid4()),
            belief_id=belief_id,
            case_id=case_id,
            scope=scope,
            admissible=admissible,
            hard_violations=hard_violations,
            soft_conflicts=soft_conflicts,
            timestamp=time.time(),
        )