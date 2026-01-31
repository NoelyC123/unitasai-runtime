from dataclasses import dataclass
from typing import List
from uuid import UUID
from src.invariants.invariant_types import InvariantStrength


@dataclass(frozen=True)
class InvariantViolation:
    invariant_id: UUID
    strength: InvariantStrength
    reason: str


@dataclass(frozen=True)
class InvariantPreCheckResult:
    blocked: bool
    hard_violations: List[InvariantViolation]
    soft_violations: List[InvariantViolation]
