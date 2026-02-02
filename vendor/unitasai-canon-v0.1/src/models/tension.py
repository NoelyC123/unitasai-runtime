from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class Tension:
    """
    Canon v0.1 — Tension Artifact
    Phase: 21C
    """

    tension_id: UUID
    case_id: UUID

    tension_type: str  # Canon enum; deferred
    participant_beliefs: list[UUID]

    status: str  # active | resolved | superseded
    created_at: datetime

    resolved_at: datetime | None = None
    resolved_by: str | None = None
    superseded_by: UUID | None = None
