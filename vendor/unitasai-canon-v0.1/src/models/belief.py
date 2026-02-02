from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class Belief:
    """
    Canon v0.1 — Belief Artifact
    Phase: 21B / 21C / 21D / 23
    """

    belief_id: UUID
    case_id: UUID

    text: str
    scope: str  # Canon enum; values not resolved here
    status: str  # active | revised | invalidated
    confidence: float  # semantics deferred (Canon v0.1)

    created_at: datetime
    created_by: str

    superseded_by: UUID | None = None
