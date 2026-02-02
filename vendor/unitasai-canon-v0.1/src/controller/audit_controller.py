from uuid import UUID

from src.controller.controller_context import ControllerContext


class AuditController:
    """
    Canon v0.1 — Audit Controller
    Centralised audit emission authority.
    """

    def emit(
        self,
        *,
        event_type: str,
        case_id: UUID | None,
        artifact_id: UUID | None,
        metadata: dict[str, str],
        context: ControllerContext,
    ) -> None:
        context.audit_store.emit(
            event_type=event_type,
            case_id=case_id,
            artifact_id=artifact_id,
            metadata=metadata,
        )
