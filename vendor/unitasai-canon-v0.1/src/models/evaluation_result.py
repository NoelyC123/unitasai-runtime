from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass(frozen=True)
class EvaluationResult:
    """
    Canon v0.1 — Evaluation Result
    Phase: 21B
    """

    evaluation_id: UUID
    belief_id: UUID
    case_id: UUID

    evaluation_status: str     # supported | unsupported | indeterminate
    evaluation_basis: str      # structured descriptor (no narrative)

    created_at: datetime
