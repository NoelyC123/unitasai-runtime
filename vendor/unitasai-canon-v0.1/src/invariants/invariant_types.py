from dataclasses import dataclass
from enum import Enum
from typing import Any
from uuid import UUID


class InvariantSeverity(str, Enum):
    HARD = "hard"
    SOFT = "soft"


@dataclass(frozen=True)
class InvariantDefinition:
    """
    Canon v0.1 — Invariant Definition
    Phase 22
    """

    invariant_id: UUID
    name: str
    severity: InvariantSeverity
    description: str


@dataclass(frozen=True)
class InvariantViolation:
    """
    Canon v0.1 — Invariant Violation Record
    """

    invariant_id: UUID
    severity: InvariantSeverity
    violated_by: UUID  # belief_id or case_id
    context: dict[str, Any]
