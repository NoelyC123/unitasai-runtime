from uuid import uuid4, UUID
from datetime import datetime
from typing import List

from src.tensions.tension_types import (
    Tension,
    TensionType,
    TensionStatus,
)
from src.controller.controller_context import ControllerContext


class TensionEngine:
    """
    Canon v0.1 — Tension Detection Engine
    Phase 21C (Detection only)

    No resolution logic.
    No belief mutation.
    No prioritisation.
    """

    def detect_for_belief(
        self,
        belief_id: UUID,
        context: ControllerContext,
    ) -> List[Tension]:

        belief = context.belief_store.get(belief_id)
        existing_beliefs = context.belief_store.list_for_case(belief.case_id)

        detected: List[Tension] = []

        for other in existing_beliefs:
            if other.belief_id == belief.belief_id:
                continue

            # Minimal contradiction heuristic (Canon-safe placeholder)
            if belief.text == other.text and belief.scope != other.scope:
                detected.append(
                    Tension(
                        tension_id=uuid4(),
                        case_id=belief.case_id,
                        tension_type=TensionType.SCOPE_CONFLICT,
                        participants=[belief.belief_id, other.belief_id],
                        status=TensionStatus.ACTIVE,
                        description="Beliefs share text but differ in scope",
                        created_at=datetime.utcnow(),
                        resolved_at=None,
                        superseded_by=None,
                    )
                )

        return detected
