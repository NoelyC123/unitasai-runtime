from dataclasses import dataclass
from uuid import UUID
from typing import Optional, List
from src.intake.intake_errors import IntakeFailureReason


@dataclass(frozen=True)
class BeliefIntakeRequest:
    request_id: UUID
    case_id: UUID
    text: str
    scope: str
    confidence: Optional[float]


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
    artifact_id: Optional[UUID]
    failure_reason: Optional[IntakeFailureReason]
    warnings: List[str]
