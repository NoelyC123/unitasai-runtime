from dataclasses import dataclass
from typing import Optional
from uuid import UUID
from datetime import datetime


@dataclass(frozen=True)
class Justification:
    """
    Canon v0.1 — Justification Artifact
    Phase: 23
    """

    justification_id: UUID
    belief_id: UUID
    case_id: UUID

    content: str
    source_type: str        # Canon enum; deferred
    scope: str

    created_at: datetime
    created_by: str

    withdrawn_at: Optional[datetime] = None
