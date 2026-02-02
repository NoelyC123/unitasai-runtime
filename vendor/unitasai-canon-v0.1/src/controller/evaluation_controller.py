from uuid import UUID

from src.controller.controller_context import ControllerContext
from src.evaluation.evaluation_engine import EvaluationEngine


class EvaluationController:
    """
    Canon v0.1 — Evaluation Controller
    Phase 21B
    """

    def __init__(self) -> None:
        self.engine = EvaluationEngine()

    def evaluate_belief(
        self,
        belief_id: UUID,
        context: ControllerContext,
    ) -> None:
        context.audit_store.emit_evaluation_invoked(
            belief_id=belief_id,
        )

        evaluation = self.engine.evaluate_belief(
            belief_id=belief_id,
            context=context,
        )

        context.evaluation_store.persist(evaluation)

        context.audit_store.emit_evaluation_completed(
            evaluation_id=evaluation.evaluation_id,
            belief_id=belief_id,
            evaluation_status=evaluation.evaluation_status.value,
        )
