from enum import Enum


class IntakeFailureReason(str, Enum):
    VALIDATION_FAILED = "validation_failed"
    INADMISSIBLE = "inadmissible"
    BLOCKED = "blocked"
    REJECTED = "rejected"
    DEFERRED = "deferred"
