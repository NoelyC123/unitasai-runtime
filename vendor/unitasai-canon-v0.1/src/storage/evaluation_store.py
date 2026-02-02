from typing import Protocol
from uuid import UUID

from src.models.evaluation_result import EvaluationResult


class EvaluationStore(Protocol):
    """
    Canon v0.1 — Evaluation Result Store
    Phase: 21B
    """

    def list_for_belief(self, belief_id: UUID) -> list[EvaluationResult]: ...

    def insert(self, evaluation: EvaluationResult) -> None: ...
