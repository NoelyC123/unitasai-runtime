from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class RevisionEvent:
    """
    Canon v0.1 — Revision Event
    Phase: 21D
    """

    revision_id: UUID
    case_id: UUID

    revision_type: str  # status_change | confidence_adjustment | scope_correction | composite
    triggered_by: UUID  # artifact reference

    affected_beliefs: list[UUID]
    affected_tensions: list[UUID]

    minimal_change_score: int
    alternatives_considered: int

    created_at: datetime
    created_by: str
