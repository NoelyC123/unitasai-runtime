from src.controller.controller_context import ControllerContext
from src.intake.intake_engine import IntakeEngine
from src.intake.intake_errors import IntakeFailureReason
from src.intake.intake_types import BeliefIntakeRequest, IntakeOutcome
from src.invariants.invariant_controller import InvariantController
from src.invariants.invariant_types import InvariantDefinition


class IntakeController:
    """
    Canon v0.1 — Intake Controller
    Phase 23

    Enforces invariant gates before intake.
    """

    def __init__(self) -> None:
        self._engine = IntakeEngine()
        self._invariants = InvariantController()

    def submit_belief(
        self,
        request: BeliefIntakeRequest,
        invariants: list[InvariantDefinition],
        context: ControllerContext,
    ) -> IntakeOutcome:
        violations = self._invariants.evaluate_case_invariants(
            case_id=request.case_id,
            invariants=invariants,
            context=context,
        )

        if self._invariants.has_hard_violation(violations):
            context.audit_store.emit_intake_blocked(
                case_id=request.case_id,
                reason="hard_invariant_violation",
            )
            return IntakeOutcome(
                request_id=request.request_id,
                admitted=False,
                artifact_id=None,
                failure_reason=IntakeFailureReason.INVARIANT_BLOCK,
                warnings=[],
            )

        return self._engine.submit_belief(
            request=request,
            context=context,
        )
