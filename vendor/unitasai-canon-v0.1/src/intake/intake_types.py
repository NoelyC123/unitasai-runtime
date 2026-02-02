from dataclasses import dataclass
from uuid import UUID

from src.intake.intake_errors import IntakeFailureReason


@dataclass(frozen=True)
class BeliefIntakeRequest:
    request_id: UUID
    case_id: UUID
    text: str
    scope: str
    confidence: float | None


@dataclass(frozen=True)
class JustificationIntakeRequest:
    request_id: UUID
    belief_id: UUID
    content: str
    justification_type: str


@dataclass(frozen=True)
class IntakeOutcome:
    request_id: UUID
    admitted: bool
    artifact_id: UUID | None
    failure_reason: IntakeFailureReason | None
    warnings: list[str]
