from uuid import UUID

from src.controller.controller_context import ControllerContext
from src.revision.revision_types import BeliefStateChange, RevisionCandidate


class RevisionExecutor:
    """
    Canon v0.1 — Revision Execution Engine
    Phase 21D

    Executes an explicitly authorized RevisionCandidate.
    Does NOT decide which candidate to use.
    """

    def execute(
        self,
        revision_id: UUID,
        candidate: RevisionCandidate,
        context: ControllerContext,
    ) -> None:
        for change in candidate.affected_beliefs:
            self._apply_belief_change(change, context)

        context.revision_store.persist_revision_event(
            revision_id=revision_id,
            revision_type=candidate.revision_type,
            affected_beliefs=candidate.affected_beliefs,
            minimal_change_score=candidate.minimal_change_score,
        )

    def _apply_belief_change(
        self,
        change: BeliefStateChange,
        context: ControllerContext,
    ) -> None:
        if change.field_changed == "status":
            context.belief_store.update_status(
                belief_id=change.belief_id,
                new_status=change.new_value,
            )

        elif change.field_changed == "confidence":
            context.belief_store.update_confidence(
                belief_id=change.belief_id,
                new_confidence=float(change.new_value),
            )

        elif change.field_changed == "scope":
            context.belief_store.update_scope(
                belief_id=change.belief_id,
                new_scope=change.new_value,
            )

        else:
            raise ValueError(f"Unsupported belief field change: {change.field_changed}")
