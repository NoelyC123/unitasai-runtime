"""
Phase 21B++c — Temporal Authority Drift Windows (helper module)

Read-only. Descriptive only. No mutation. No new authority.

This module computes fixed-time windows over *existing* audit-derived drift signals:

1) Evaluation admission signal:
   - action: "EVALUATION"
   - payload field: "is_admissible" (bool)
   - window metric: admission_ratio = admitted / total_evaluations

2) Controller deference signal:
   - action: "CONTROLLER_DECISION"
   - payload field: "decision" == "approved"
   - window metric: controller_deference_ratio = approved / total_decisions

Drift between adjacent windows is computed as a simple, auditable L1 delta over
available ratio values.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any

# ─────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────


@dataclass(frozen=True)
class TemporalWindowConfig:
    window_seconds: int = 300
    drift_threshold: float = 0.25


# ─────────────────────────────────────────────
# Public entrypoint
# ─────────────────────────────────────────────


def compute_temporal_windows(
    audit_events: list[dict[str, Any]],
    *,
    config: TemporalWindowConfig | None = None,
) -> dict[str, Any]:
    cfg = config or TemporalWindowConfig()

    normalized: list[tuple[float, dict[str, Any]]] = []
    for e in audit_events:
        ts = _parse_timestamp(e.get("timestamp"))
        if ts is None:
            continue
        normalized.append((ts, e))

    if not normalized:
        return {
            "config": {
                "window_seconds": cfg.window_seconds,
                "drift_threshold": cfg.drift_threshold,
            },
            "windows": [],
            "episodes": [],
            "metrics": {
                "window_count": 0,
                "episode_count": 0,
                "note": "No events with parseable timestamps.",
            },
        }

    normalized.sort(key=lambda x: x[0])

    start_ts = _align_start(normalized[0][0], cfg.window_seconds)
    end_ts = normalized[-1][0]

    bins = _build_bins(
        start_ts=start_ts,
        end_ts=end_ts,
        window_seconds=cfg.window_seconds,
    )

    windows: list[dict[str, Any]] = []
    idx = 0

    for w_start, w_end in bins:
        evs: list[dict[str, Any]] = []
        while idx < len(normalized) and normalized[idx][0] < w_end:
            if normalized[idx][0] >= w_start:
                evs.append(normalized[idx][1])
            idx += 1
        windows.append(_compute_window(w_start, w_end, evs))

    prev = None
    for w in windows:
        if prev is None:
            w["drift"] = None
            w["drift_components"] = None
            prev = w
            continue

        drift, comps = _compute_drift(prev, w)
        w["drift"] = drift
        w["drift_components"] = comps
        prev = w

    episodes = _compute_episodes(
        windows,
        drift_threshold=cfg.drift_threshold,
    )

    metrics = {
        "window_count": len(windows),
        "episode_count": len(episodes),
        "max_drift": _max_drift(windows),
        "mean_drift": _mean_drift(windows),
        "note": "Descriptive only. Drift is L1 delta over available ratio changes.",
    }

    return {
        "config": {
            "window_seconds": cfg.window_seconds,
            "drift_threshold": cfg.drift_threshold,
        },
        "windows": windows,
        "episodes": episodes,
        "metrics": metrics,
    }


# ─────────────────────────────────────────────
# Window computation
# ─────────────────────────────────────────────


def _compute_window(
    start_ts: float,
    end_ts: float,
    events: list[dict[str, Any]],
) -> dict[str, Any]:
    eval_total = 0
    eval_admitted = 0
    decision_total = 0
    decision_approved = 0

    for e in events:
        action = e.get("action")
        payload = e.get("payload") or {}

        if action == "EVALUATION":
            eval_total += 1
            if payload.get("is_admissible") is True:
                eval_admitted += 1

        elif action == "CONTROLLER_DECISION":
            decision_total += 1
            if payload.get("decision") == "approved":
                decision_approved += 1

    return {
        "window_start": _ts_to_iso(start_ts),
        "window_end": _ts_to_iso(end_ts),
        "window_start_ts": start_ts,
        "window_end_ts": end_ts,
        "event_count": len(events),
        "evaluation_count": eval_total,
        "admitted_evaluations": eval_admitted,
        "admission_ratio": (eval_admitted / eval_total if eval_total else None),
        "controller_decision_count": decision_total,
        "approved_decisions": decision_approved,
        "controller_deference_ratio": (
            decision_approved / decision_total if decision_total else None
        ),
    }


# ─────────────────────────────────────────────
# Drift logic
# ─────────────────────────────────────────────


def _compute_drift(
    prev: dict[str, Any],
    cur: dict[str, Any],
) -> tuple[float, dict[str, float | None]]:
    da = _delta(prev.get("admission_ratio"), cur.get("admission_ratio"))
    dd = _delta(
        prev.get("controller_deference_ratio"),
        cur.get("controller_deference_ratio"),
    )

    drift = 0.0
    if da is not None:
        drift += abs(da)
    if dd is not None:
        drift += abs(dd)

    return drift, {
        "delta_admission_ratio": da,
        "delta_controller_deference_ratio": dd,
    }


def _delta(x: Any, y: Any) -> float | None:
    if x is None or y is None:
        return None
    try:
        return float(y) - float(x)
    except (TypeError, ValueError):
        return None


# ─────────────────────────────────────────────
# Episode detection
# ─────────────────────────────────────────────


def _compute_episodes(
    windows: list[dict[str, Any]],
    *,
    drift_threshold: float,
) -> list[dict[str, Any]]:
    episodes: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None

    for i, w in enumerate(windows):
        drift = w.get("drift")
        hot = drift is not None and drift > drift_threshold

        if hot and current is None:
            current = {
                "start_index": i,
                "end_index": i,
                "start_window": w["window_start"],
                "end_window": w["window_end"],
                "window_count": 1,
                "max_drift": drift,
            }
        elif hot and current is not None:
            current["end_index"] = i
            current["end_window"] = w["window_end"]
            current["window_count"] += 1
            if drift > current["max_drift"]:
                current["max_drift"] = drift
        elif not hot and current is not None:
            episodes.append(current)
            current = None

    if current is not None:
        episodes.append(current)

    return episodes


# ─────────────────────────────────────────────
# Metrics helpers
# ─────────────────────────────────────────────


def _max_drift(windows: list[dict[str, Any]]) -> float:
    vals = [w["drift"] for w in windows if w.get("drift") is not None]
    return max(vals) if vals else 0.0


def _mean_drift(windows: list[dict[str, Any]]) -> float:
    vals = [w["drift"] for w in windows if w.get("drift") is not None]
    return sum(vals) / len(vals) if vals else 0.0


# ─────────────────────────────────────────────
# Time utilities
# ─────────────────────────────────────────────


def _build_bins(
    *,
    start_ts: float,
    end_ts: float,
    window_seconds: int,
) -> list[tuple[float, float]]:
    bins: list[tuple[float, float]] = []
    cur = start_ts
    while cur <= end_ts:
        nxt = cur + float(window_seconds)
        bins.append((cur, nxt))
        cur = nxt
    return bins


def _align_start(ts: float, window_seconds: int) -> float:
    ws = float(window_seconds)
    return (ts // ws) * ws


def _parse_timestamp(v: Any) -> float | None:
    if v is None:
        return None
    if isinstance(v, int | float):
        return float(v) if v > 0 else None
    if isinstance(v, datetime):
        dt = v if v.tzinfo else v.replace(tzinfo=UTC)
        return dt.timestamp()
    if isinstance(v, str):
        try:
            dt = datetime.fromisoformat(v.replace("Z", "+00:00"))
            dt = dt if dt.tzinfo else dt.replace(tzinfo=UTC)
            return dt.timestamp()
        except ValueError:
            return None
    return None


def _ts_to_iso(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=UTC).isoformat()
