"""
Canon v0.1 — Integrity Guardrails

These guards prevent:
- Silent canon violations
- Underspecified behaviour creep
- Controller bypassing
"""


class CanonViolation(RuntimeError):
    """Raised when Canon v0.1 is violated."""

    pass


def forbid(message: str) -> None:
    """
    Immediately terminate execution for forbidden paths.
    """
    raise CanonViolation(message)


def require(condition: bool, message: str) -> None:
    """
    Assert a Canon-required condition.
    """
    if not condition:
        raise CanonViolation(message)


def forbid_underspecified(area_id: str) -> None:
    """
    Guard against accidental resolution of underspecified Canon areas.
    """
    raise CanonViolation(f"Underspecified Canon area accessed without version bump: {area_id}")
