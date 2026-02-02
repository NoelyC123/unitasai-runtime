"""
Pure metric computations for RADO.

IMPORTANT:
- Metrics compute quantities only
- Metrics do NOT interpret results
- Metrics do NOT classify or evaluate safety
"""

from collections.abc import Iterable
from typing import Any


def count_actions(events: Iterable[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for e in events:
        action = e.get("action", "UNKNOWN")
        counts[action] = counts.get(action, 0) + 1
    return counts
