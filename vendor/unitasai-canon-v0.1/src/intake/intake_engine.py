from uuid import UUID
from typing import List

from src.intake.intake_types import (
    BeliefIntakeRequest,
    JustificationIntakeRequest,
    IntakeOutcome,
    IntakeOutcomeType,
)
from src.intake.intake_errors import IntakeFailureReason
from src.controller.controller_context import ControllerContext


class IntakeEngine:
    """
    Canon v0.1 — Intake Pipeline Engine
    Phase 23 (Design-locked)

    This engine performs:
    - Structural validation
    - Admissibility checks (non-semantic)
    - Delegation to controller for authorization
    - Admission & persistence
    - Mandatory audit emission
    """

    def submit_belief(
        self,
        request: BeliefIntakeRequest,
        context: ControllerContext,
        authorized: bool,
    ) -> IntakeOutcome:
        """
        Submit a belief intake request.
        Authorization MUST be explicit.
        """

        # ─────────────────────────────
        # Stage 0 — Audit: request received
        # ─────────────────────────────
        context.audit_store.emit_intake_request_received(
            request_id=request.request_id,
            case_id=request.case_id,
            request_type="belief",
        )

        # ─────────────────────────────
        # Stage 1 — Validation
        # ─────────────────────────────
        if not request.proposed_text or not request.case_id:
            context.audit_store.emit_intake_validation_failed(
                request_id=request.request_id,
                reason="missing required fields",
            )
            return IntakeOutcome(
                request_id=request.request_id,
                outcome=IntakeOutcomeType.VALIDATION_FAILED,
                artifact_id=None,
                failure_reason=IntakeFailureReason.VALIDATION_FAILED,
                warnings=[],
            )

        # ─────────────────────────────
        # Stage 2 — Admissibility
        # (Exact, non-semantic only)
        # ─────────────────────────────
        # Duplicate detection / scope coherence deferred per Canon

        # ─────────────────────────────
        # Stage 3 — Invariant Pre-Check
        # (Delegated; not implemented here)
        # ─────────────────────────────

        # ─────────────────────────────
        # Stage 4 — Controller Authorization
        # ─────────────────────────────
        if not authorized:
            context.audit_store.emit_intake_rejected(
                request_id=request.request_id,
                reason="controller_not_authorized",
            )
            return IntakeOutcome(
                request_id=request.request_id,
                outcome=IntakeOutcomeType.REJECTED,
                artifact_id=None,
                failure_reason=IntakeFailureReason.REJECTED,
                warnings=[],
            )

        # ─────────────────────────────
        # Stage 5 — Admission & Persistence
        # ─────────────────────────────
        belief_id: UUID = context.belief_store.create(
            case_id=request.case_id,
            text=request.proposed_text,
            scope=request.proposed_scope,
            confidence=request.proposed_confidence,
        )

        # ─────────────────────────────
        # Stage 6 — Audit Emission
        # ─────────────────────────────
        context.audit_store.emit_belief_created(
            belief_id=belief_id,
            case_id=request.case_id,
            scope=request.proposed_scope,
        )

        return IntakeOutcome(
            request_id=request.request_id,
            outcome=IntakeOutcomeType.ADMITTED,
            artifact_id=belief_id,
            failure_reason=None,
            warnings=[],
        )

    def submit_justification(
        self,
        request: JustificationIntakeRequest,
        context: ControllerContext,
        authorized: bool,
    ) -> IntakeOutcome:
        """
        Submit a justification intake request.
        """

        context.audit_store.emit_intake_request_received(
            request_id=request.request_id,
            case_id=request.case_id,
            request_type="justification",
        )

        if not request.proposed_content or not request.target_belief_id:
            context.audit_store.emit_intake_validation_failed(
                request_id=request.request_id,
                reason="missing required fields",
            )
            return IntakeOutcome(
                request_id=request.request_id,
                outcome=IntakeOutcomeType.VALIDATION_FAILED,
                artifact_id=None,
                failure_reason=IntakeFailureReason.VALIDATION_FAILED,
                warnings=[],
            )

        if not authorized:
            context.audit_store.emit_intake_rejected(
                request_id=request.request_id,
                reason="controller_not_authorized",
            )
            return IntakeOutcome(
                request_id=request.request_id,
                outcome=IntakeOutcomeType.REJECTED,
                artifact_id=None,
                failure_reason=IntakeFailureReason.REJECTED,
                warnings=[],
            )

        justification_id: UUID = context.justification_store.create(
            belief_id=request.target_belief_id,
            content=request.proposed_content,
            justification_type=request.justification_type,
        )

        context.audit_store.emit_justification_created(
            justification_id=justification_id,
            belief_id=request.target_belief_id,
            case_id=request.case_id,
        )

        return IntakeOutcome(
            request_id=request.request_id,
            outcome=IntakeOutcomeType.ADMITTED,
            artifact_id=justification_id,
            failure_reason=None,
            warnings=[],
        )
