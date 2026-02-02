from src.controller.controller_context import ControllerContext
from src.invariants.invariant_types import (
    InvariantDefinition,
    InvariantViolation,
)


class InvariantEngine:
    """
    Canon v0.1 — Invariant Evaluation Engine
    Phase 22

    Evaluates invariants.
    Produces violations.
    Performs NO mutation.
    """

    def evaluate_case(
        self,
        case_id,
        invariants: list[InvariantDefinition],
        context: ControllerContext,
    ) -> list[InvariantViolation]:
        violations: list[InvariantViolation] = []

        for invariant in invariants:
            violated = self._check_invariant(invariant, case_id, context)

            if violated:
                violations.append(
                    InvariantViolation(
                        invariant_id=invariant.invariant_id,
                        severity=invariant.severity,
                        violated_by=case_id,
                        context={"case_id": str(case_id)},
                    )
                )

        return violations

    def _check_invariant(
        self,
        invariant: InvariantDefinition,
        case_id,
        context: ControllerContext,
    ) -> bool:
        """
        Placeholder predicate.
        Canon v0.1 does not specify predicate language.
        """

        # Explicitly underspecified → always return False
        return False
