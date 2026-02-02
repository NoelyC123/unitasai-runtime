"""
Phase 21C — Stability & Recovery Metrics (helper)

Read-only. Descriptive only.
Consumes Phase 21B temporal windows and episodes.
"""

from __future__ import annotations

from statistics import mean, variance
from typing import Any


def compute_stability_and_recovery(
    *,
    windows: list[dict[str, Any]],
    episodes: list[dict[str, Any]],
    drift_threshold: float,
) -> dict[str, Any]:
    drifts = [w.get("drift") for w in windows if w.get("drift") is not None]

    stability_index = None
    if len(drifts) >= 2:
        try:
            stability_index = 1.0 / (variance(drifts) + 1e-9)
        except Exception:
            stability_index = None

    oscillations = _count_oscillations(drifts)

    recovery_windows = _compute_recovery_windows(windows, episodes, drift_threshold)

    return {
        "stability_index": stability_index,
        "oscillation_count": oscillations,
        "mean_recovery_windows": mean(recovery_windows) if recovery_windows else None,
        "max_recovery_windows": max(recovery_windows) if recovery_windows else None,
        "note": "Descriptive only. No decisions or control influence.",
    }


def _count_oscillations(drifts: list[float]) -> int:
    count = 0
    last_sign: int | None = None
    for d in drifts:
        sign = 1 if d > 0 else -1 if d < 0 else 0
        if last_sign is not None and sign != 0 and sign != last_sign:
            count += 1
        if sign != 0:
            last_sign = sign
    return count


def _compute_recovery_windows(
    windows: list[dict[str, Any]],
    episodes: list[dict[str, Any]],
    drift_threshold: float,
) -> list[int]:
    recoveries: list[int] = []
    for ep in episodes:
        end_idx = ep.get("end_index")
        if end_idx is None:
            continue
        steps = 0
        for w in windows[end_idx + 1 :]:
            steps += 1
            d = w.get("drift")
            if d is not None and d <= drift_threshold:
                recoveries.append(steps)
                break
    return recoveries
