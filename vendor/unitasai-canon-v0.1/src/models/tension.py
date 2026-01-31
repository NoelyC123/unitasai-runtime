from dataclasses import dataclass
from typing import List, Optional
from uuid import UUID
from datetime import datetime


@dataclass(frozen=True)
class Tension:
    """
    Canon v0.1 — Tension Artifact
    Phase: 21C
    """

    tension_id: UUID
    case_id: UUID

    tension_type: str                 # Canon enum; deferred
    participant_beliefs: List[UUID]

    status: str                       # active | resolved | superseded
    created_at: datetime

    resolved_at: Optional[datetime] = None
    resolved_by: Optional[str] = None
    superseded_by: Optional[UUID] = None
