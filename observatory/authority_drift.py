"""
Runtime Authority Drift Observatory (RADO)

NON-AUTHORITY MODULE

This module performs post-hoc analysis of audit records to describe
patterns related to evaluation deference and controller behaviour.

It does NOT:
- Decide
- Recommend
- Enforce
- Warn
- Block
- Intervene

All outputs are descriptive only.
"""

from typing import Iterable, Dict, Any


class AuthorityDriftObservatory:
    """
    Read-only observatory over audit events.

    This class MUST NOT:
    - Mutate state
    - Emit audit events
    - Influence control flow
    """

    def __init__(self, audit_events: Iterable[Dict[str, Any]]):
        # Audit events are assumed to be immutable historical records
        self._events = list(audit_events)

    def snapshot(self) -> Dict[str, Any]:
        """
        Returns a raw snapshot summary of available audit data.

        This method intentionally performs no interpretation,
        scoring, classification, or judgment.
        """
        return {
            "total_events": len(self._events),
            "event_types": sorted({e.get("action", "UNKNOWN") for e in self._events}),
        }