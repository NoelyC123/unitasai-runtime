from dataclasses import dataclass
from typing import List
from uuid import UUID
from datetime import datetime


@dataclass(frozen=True)
class RevisionEvent:
    """
    Canon v0.1 — Revision Event
    Phase: 21D
    """

    revision_id: UUID
    case_id: UUID

    revision_type: str                # status_change | confidence_adjustment | scope_correction | composite
    triggered_by: UUID                # artifact reference

    affected_beliefs: List[UUID]
    affected_tensions: List[UUID]

    minimal_change_score: int
    alternatives_considered: int

    created_at: datetime
    created_by: str
