from dataclasses import dataclass
from enum import Enum
from typing import List, Optional
from uuid import UUID
from datetime import datetime


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
    participants: List[UUID]
    status: TensionStatus
    description: str
    created_at: datetime
    resolved_at: Optional[datetime]
    superseded_by: Optional[UUID]
