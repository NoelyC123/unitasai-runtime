from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class EvaluationResult:
    """
    Canon v0.1 — Evaluation Result
    Phase: 21B
    """

    evaluation_id: UUID
    belief_id: UUID
    case_id: UUID

    evaluation_status: str  # supported | unsupported | indeterminate
    evaluation_basis: str  # structured descriptor (no narrative)

    created_at: datetime
