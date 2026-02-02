from uuid import UUID

from src.controller.controller_context import ControllerContext
from src.revision.revision_types import (
    BeliefStateChange,
    RevisionCandidate,
    RevisionType,
)


class RevisionEngine:
    """
    Canon v0.1 — Revision Candidate Enumeration Engine
    Phase 21D (Enumeration only)

    Does NOT:
    - Execute revisions
    - Modify beliefs
    - Resolve tensions
    """

    def enumerate_candidates_for_belief(
        self,
        belief_id: UUID,
        context: ControllerContext,
    ) -> list[RevisionCandidate]:
        belief = context.belief_store.get(belief_id)

        candidates: list[RevisionCandidate] = []

        # Candidate 1: Invalidate belief
        candidates.append(
            RevisionCandidate(
                revision_type=RevisionType.STATUS_CHANGE,
                affected_beliefs=[
                    BeliefStateChange(
                        belief_id=belief.belief_id,
                        field_changed="status",
                        previous_value=belief.status,
                        new_value="invalidated",
                        change_reason="Hard invariant or unresolved tension",
                    )
                ],
                minimal_change_score=1,
            )
        )

        # Candidate 2: Lower confidence (placeholder semantics)
        candidates.append(
            RevisionCandidate(
                revision_type=RevisionType.CONFIDENCE_ADJUSTMENT,
                affected_beliefs=[
                    BeliefStateChange(
                        belief_id=belief.belief_id,
                        field_changed="confidence",
                        previous_value=str(belief.confidence),
                        new_value="0.0",
                        change_reason="Confidence reduction to restore consistency",
                    )
                ],
                minimal_change_score=1,
            )
        )

        return candidates
