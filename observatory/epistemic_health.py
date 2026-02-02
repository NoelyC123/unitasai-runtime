"""
Phase 22 — Epistemic Health Index (helper)

Read-only. Descriptive only.
Aggregates existing observability metrics.
"""

from __future__ import annotations

from typing import Any


def compute_epistemic_health_index(
    *,
    temporal: dict[str, Any],
    correlation: dict[str, Any],
    stability: dict[str, Any],
) -> dict[str, Any]:
    windows = temporal.get("windows", [])
    episodes = temporal.get("episodes", [])

    drifts = [w.get("drift") for w in windows if w.get("drift") is not None]

    return {
        "drift_health": {
            "window_count": len(windows),
            "episode_count": len(episodes),
            "mean_drift": sum(drifts) / len(drifts) if drifts else None,
            "max_drift": max(drifts) if drifts else None,
        },
        "stability_health": {
            "stability_index": stability.get("stability_index"),
            "oscillation_count": stability.get("oscillation_count"),
            "mean_recovery_windows": stability.get("mean_recovery_windows"),
            "max_recovery_windows": stability.get("max_recovery_windows"),
        },
        "alignment_health": {
            "zero_lag_correlation": correlation.get("zero_lag", {}).get("pearson_r"),
            "best_abs_correlation": (
                correlation.get("best_abs", {}).get("pearson_r")
                if correlation.get("best_abs")
                else None
            ),
            "best_lag": (
                correlation.get("best_abs", {}).get("lag") if correlation.get("best_abs") else None
            ),
        },
        "note": "Descriptive aggregation only. No normative interpretation.",
    }
