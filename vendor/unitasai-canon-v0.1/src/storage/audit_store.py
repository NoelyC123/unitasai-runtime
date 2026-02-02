from uuid import UUID


class AuditStore:
    """
    Canon v0.1 — Audit Store Interface
    Append-only. No mutation. No deletion.
    """

    def emit(
        self,
        *,
        event_type: str,
        case_id: UUID | None,
        artifact_id: UUID | None,
        metadata: dict[str, str],
    ) -> None:
        raise NotImplementedError

    # ---- Canonical Events ----

    def emit_belief_created(self, belief_id: UUID, case_id: UUID) -> None:
        self.emit(
            event_type="belief_created",
            case_id=case_id,
            artifact_id=belief_id,
            metadata={},
        )

    def emit_justification_created(self, justification_id: UUID, belief_id: UUID) -> None:
        self.emit(
            event_type="justification_created",
            case_id=None,
            artifact_id=justification_id,
            metadata={"belief_id": str(belief_id)},
        )

    def emit_intake_blocked(self, case_id: UUID, reason: str) -> None:
        self.emit(
            event_type="intake_blocked",
            case_id=case_id,
            artifact_id=None,
            metadata={"reason": reason},
        )

    def emit_revision_blocked(self, case_id: UUID, reason: str) -> None:
        self.emit(
            event_type="revision_blocked",
            case_id=case_id,
            artifact_id=None,
            metadata={"reason": reason},
        )

    def emit_evaluation_completed(
        self,
        evaluation_id: UUID,
        belief_id: UUID,
        status: str,
    ) -> None:
        self.emit(
            event_type="evaluation_completed",
            case_id=None,
            artifact_id=evaluation_id,
            metadata={
                "belief_id": str(belief_id),
                "status": status,
            },
        )
