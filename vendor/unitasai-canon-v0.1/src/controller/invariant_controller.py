from src.controller.controller_context import ControllerContext
from src.invariants.invariant_engine import InvariantEngine
from src.invariants.invariant_types import (
    InvariantDefinition,
    InvariantSeverity,
    InvariantViolation,
)


class InvariantController:
    """
    Canon v0.1 — Invariant Controller
    Phase 22

    Interprets invariant violations.
    Does not enforce corrections.
    """

    def __init__(self) -> None:
        self._engine = InvariantEngine()

    def evaluate_case_invariants(
        self,
        case_id,
        invariants: list[InvariantDefinition],
        context: ControllerContext,
    ) -> list[InvariantViolation]:
        violations = self._engine.evaluate_case(
            case_id=case_id,
            invariants=invariants,
            context=context,
        )

        for violation in violations:
            context.audit_store.emit_invariant_violated(
                invariant_id=violation.invariant_id,
                severity=violation.severity.value,
                violated_by=violation.violated_by,
            )

        return violations

    def has_hard_violation(
        self,
        violations: list[InvariantViolation],
    ) -> bool:
        return any(v.severity == InvariantSeverity.HARD for v in violations)
