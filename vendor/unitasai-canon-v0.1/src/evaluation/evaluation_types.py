from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from uuid import UUID


class EvaluationStatus(Enum):
    SUPPORTED = "supported"
    UNSUPPORTED = "unsupported"
    CONTESTED = "contested"
    UNDERDETERMINED = "underdetermined"
    WITHDRAWN = "withdrawn"


@dataclass(frozen=True)
class StructuredReasoning:
    """
    Canon v0.1 — Structured, non-narrative reasoning
    """

    status_basis: str
    referenced_justification_ids: list[UUID]
    referenced_tension_ids: list[UUID]
    notes: str | None


@dataclass(frozen=True)
class EvaluationResult:
    """
    Canon v0.1 — Belief Evaluation Output
    """

    evaluation_id: UUID
    belief_id: UUID
    case_id: UUID
    evaluation_status: EvaluationStatus
    justification_count: int
    tension_count: int
    tension_ids: list[UUID]
    evaluated_at: datetime
    reasoning: StructuredReasoning
