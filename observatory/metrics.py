"""
Pure metric computations for RADO.

IMPORTANT:
- Metrics compute quantities only
- Metrics do NOT interpret results
- Metrics do NOT classify or evaluate safety
"""

from typing import Iterable, Dict, Any


def count_actions(events: Iterable[Dict[str, Any]]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for e in events:
        action = e.get("action", "UNKNOWN")
        counts[action] = counts.get(action, 0) + 1
    return counts