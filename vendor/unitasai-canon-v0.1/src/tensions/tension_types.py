from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from uuid import UUID


class TensionType(Enum):
    DIRECT_CONTRADICTION = "direct_contradiction"
    COMPETING_EXPLANATION = "competing_explanation"
    SCOPE_CONFLICT = "scope_conflict"
    INVARIANT_VIOLATION = "invariant_violation"


class TensionStatus(Enum):
    ACTIVE = "active"
    RESOLVED = "resolved"
    SUPERSEDED = "superseded"


@dataclass(frozen=True)
class Tension:
    """
    Canon v0.1 — Tension Artifact
    Phase 21C
    """

    tension_id: UUID
    case_id: UUID
    tension_type: TensionType
    participants: list[UUID]
    status: TensionStatus
    description: str
    created_at: datetime
    resolved_at: datetime | None
    superseded_by: UUID | None
