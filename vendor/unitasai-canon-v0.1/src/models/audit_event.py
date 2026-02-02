from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class AuditEvent:
    """
    Canon v0.1 — Audit Event
    Immutable, append-only, non-revisable
    """

    event_id: UUID
    event_type: str
    case_id: UUID | None
    artifact_id: UUID | None
    timestamp: datetime
    metadata: dict[str, str]
