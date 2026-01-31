from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass(frozen=True)
class Invariant:
    """
    Canon v0.1 — Invariant Artifact
    Phase: 22
    """

    invariant_id: UUID
    case_id: UUID

    invariant_type: str        # hard | soft
    predicate: str             # predicate language deferred

    active: bool

    created_at: datetime
