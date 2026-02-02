from datetime import datetime
from uuid import UUID, uuid4

from src.controller.controller_context import ControllerContext
from src.evaluation.evaluation_types import (
    EvaluationResult,
    EvaluationStatus,
    StructuredReasoning,
)


class EvaluationEngine:
    """
    Canon v0.1 — Belief Evaluation Engine
    Phase 21B

    Mechanistic. Deterministic. Read-only.
    """

    def evaluate_belief(
        self,
        belief_id: UUID,
        context: ControllerContext,
    ) -> EvaluationResult:
        belief = context.belief_store.get(belief_id)
        justifications = context.justification_store.list_for_belief(belief_id)
        tensions = context.tension_store.list_for_belief(belief_id)

        justification_count = len(justifications)
        tension_count = len(tensions)
        tension_ids = [t.tension_id for t in tensions]

        # ─────────────────────────────
        # Status determination (Canon rules)
        # ─────────────────────────────

        if belief.status in ("invalidated", "revised"):
            status = EvaluationStatus.WITHDRAWN
            basis = "belief_status"

        elif justification_count == 0:
            status = EvaluationStatus.UNSUPPORTED
            basis = "justification_absence"

        elif tension_count > 0 and justification_count > 0:
            status = EvaluationStatus.CONTESTED
            basis = "tension_participation"

        else:
            status = EvaluationStatus.SUPPORTED
            basis = "justification_presence"

        reasoning = StructuredReasoning(
            status_basis=basis,
            referenced_justification_ids=[j.justification_id for j in justifications],
            referenced_tension_ids=tension_ids,
            notes=None,
        )

        evaluation = EvaluationResult(
            evaluation_id=uuid4(),
            belief_id=belief_id,
            case_id=belief.case_id,
            evaluation_status=status,
            justification_count=justification_count,
            tension_count=tension_count,
            tension_ids=tension_ids,
            evaluated_at=datetime.utcnow(),
            reasoning=reasoning,
        )

        return evaluation
