from typing import Protocol, List
from uuid import UUID
from src.models.evaluation_result import EvaluationResult


class EvaluationStore(Protocol):
    """
    Canon v0.1 — Evaluation Result Store
    Phase: 21B
    """

    def list_for_belief(self, belief_id: UUID) -> List[EvaluationResult]:
        ...

    def insert(self, evaluation: EvaluationResult) -> None:
        ...
