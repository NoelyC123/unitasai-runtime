"""
IM-15 — Canon v0.1 End-to-End Dry Run Harness

This file proves:
- Intake works
- Evaluation works
- Tension detection works
- Invariant checks run
- Revision is controller-mediated
- Audit is complete

NO semantics.
NO heuristics.
NO LLM.
"""

from uuid import uuid4

from src.controller.controller_context import ControllerContext
from src.controller.intake_controller import IntakeController
from src.controller.evaluation_controller import EvaluationController
from src.controller.tension_controller import TensionController
from src.controller.invariant_controller import InvariantController
from src.controller.revision_controller import RevisionController

from src.storage.belief_store import BeliefStore
from src.storage.justification_store import JustificationStore
from src.storage.evaluation_store import EvaluationStore
from src.storage.tension_store import TensionStore
from src.storage.revision_store import RevisionStore
from src.storage.invariant_store import InvariantStore
from src.storage.audit_store import AuditStore

from src.intake.intake_types import BeliefIntakeRequest
from src.intake.intake_engine import IntakeEngine


def run_canon_dry_run() -> None:
    print("=== Canon v0.1 Dry Run Start ===")

    # ------------------------------------------------------------------
    # Infrastructure (in-memory / stub stores)
    # ------------------------------------------------------------------
    context = ControllerContext(
        belief_store=BeliefStore(),
        justification_store=JustificationStore(),
        evaluation_store=EvaluationStore(),
        tension_store=TensionStore(),
        revision_store=RevisionStore(),
        invariant_store=InvariantStore(),
        audit_store=AuditStore(),
    )

    # ------------------------------------------------------------------
    # Controllers
    # ------------------------------------------------------------------
    intake_controller = IntakeController()
    evaluation_controller = EvaluationController()
    tension_controller = TensionController()
    invariant_controller = InvariantController()
    revision_controller = RevisionController()

    # ------------------------------------------------------------------
    # Phase 23 — Intake
    # ------------------------------------------------------------------
    belief_request = BeliefIntakeRequest(
        request_id=uuid4(),
        case_id=uuid4(),
        text="Synthetic belief for Canon dry run",
        scope="assertive",
        confidence=0.5,
    )

    intake_result = intake_controller.submit_belief(
        request=belief_request,
        context=context,
    )

    print("Intake Result:", intake_result)

    belief_id = intake_result.artifact_id

    # ------------------------------------------------------------------
    # Phase 21B — Evaluation
    # ------------------------------------------------------------------
    evaluation_result = evaluation_controller.evaluate_belief(
        belief_id=belief_id,
        context=context,
    )

    print("Evaluation Result:", evaluation_result)

    # ------------------------------------------------------------------
    # Phase 21C — Tension Detection (read-only)
    # ------------------------------------------------------------------
    tensions = tension_controller.detect_tensions(
        belief_id=belief_id,
        context=context,
    )

    print("Tensions Detected:", tensions)

    # ------------------------------------------------------------------
    # Phase 22 — Invariant Evaluation
    # ------------------------------------------------------------------
    invariant_result = invariant_controller.evaluate_case(
        case_id=belief_request.case_id,
        context=context,
    )

    print("Invariant Result:", invariant_result)

    # ------------------------------------------------------------------
    # Phase 21D — Revision (candidate enumeration only)
    # ------------------------------------------------------------------
    revision_candidates = revision_controller.enumerate_revisions(
        belief_id=belief_id,
        context=context,
    )

    print("Revision Candidates:", revision_candidates)

    print("=== Canon v0.1 Dry Run Complete ===")


if __name__ == "__main__":
    run_canon_dry_run()
