from typing import List

from src.controller.controller_context import ControllerContext
from src.invariants.invariant_controller import InvariantController
from src.invariants.invariant_types import InvariantDefinition
from src.revision.revision_executor import RevisionExecutor
from src.revision.revision_types import RevisionPlan


class RevisionController:
    """
    Canon v0.1 — Revision Controller
    Phase 21D

    Blocks revision execution on HARD invariant violations.
    """

    def __init__(self) -> None:
        self._executor = RevisionExecutor()
        self._invariants = InvariantController()

    def execute_revision(
        self,
        plan: RevisionPlan,
        invariants: List[InvariantDefinition],
        context: ControllerContext,
    ) -> None:

        violations = self._invariants.evaluate_case_invariants(
            case_id=plan.case_id,
            invariants=invariants,
            context=context,
        )

        if self._invariants.has_hard_violation(violations):
            context.audit_store.emit_revision_blocked(
                case_id=plan.case_id,
                reason="hard_invariant_violation",
            )
            return

        self._executor.execute(plan, context)
