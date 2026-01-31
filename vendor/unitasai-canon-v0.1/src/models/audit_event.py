from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict
from uuid import UUID


@dataclass(frozen=True)
class AuditEvent:
    """
    Canon v0.1 — Audit Event
    Immutable, append-only, non-revisable
    """

    event_id: UUID
    event_type: str
    case_id: Optional[UUID]
    artifact_id: Optional[UUID]
    timestamp: datetime
    metadata: Dict[str, str]
