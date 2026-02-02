from uuid import UUID

from src.controller.controller_context import ControllerContext
from src.tensions.tension_engine import TensionEngine


class TensionController:
    """
    Canon v0.1 — Tension Controller
    Phase 21C
    """

    def __init__(self) -> None:
        self.engine = TensionEngine()

    def detect_tensions_for_belief(
        self,
        belief_id: UUID,
        context: ControllerContext,
    ) -> None:
        tensions = self.engine.detect_for_belief(
            belief_id=belief_id,
            context=context,
        )

        for tension in tensions:
            context.tension_store.persist(tension)

            context.audit_store.emit_tension_created(
                tension_id=tension.tension_id,
                case_id=tension.case_id,
                tension_type=tension.tension_type.value,
                participants=tension.participants,
            )
