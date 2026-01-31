from dataclasses import dataclass
from enum import Enum
from typing import List, Optional
from uuid import UUID


class RevisionType(Enum):
    STATUS_CHANGE = "status_change"
    CONFIDENCE_ADJUSTMENT = "confidence_adjustment"
    SCOPE_CORRECTION = "scope_correction"
    COMPOSITE = "composite"


@dataclass(frozen=True)
class BeliefStateChange:
    belief_id: UUID
    field_changed: str  # status | confidence | scope
    previous_value: str
    new_value: str
    change_reason: str


@dataclass(frozen=True)
class RevisionCandidate:
    """
    Canon v0.1 — Revision Candidate (non-executed)
    Phase 21D
    """
    revision_type: RevisionType
    affected_beliefs: List[BeliefStateChange]
    minimal_change_score: int
