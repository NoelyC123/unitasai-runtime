"""
Phase 21B++d — Temporal Drift Presentation (Text)

Presentation-only formatter for temporal authority drift data.

Rules:
- Read-only
- No computation of drift
- No mutation
- No authority
- No controller logic

This module consumes the output of:
    AuthorityDriftObservatory.temporal_authority_drift_windows()

and returns human-readable text blocks suitable for CLI output.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any


def format_temporal_summary(temporal: dict[str, Any]) -> list[str]:
    """
    Produce a compact summary block for temporal drift data.
    """
    metrics = temporal.get("metrics", {})

    lines = [
        "Temporal Drift Summary:",
        f"  Window count: {metrics.get('window_count')}",
        f"  Episode count: {metrics.get('episode_count')}",
        f"  Max drift: {metrics.get('max_drift')}",
        f"  Mean drift: {metrics.get('mean_drift')}",
    ]

    note = metrics.get("note")
    if note:
        lines.append(f"  Note: {note}")

    return lines


def format_drift_episodes(temporal: dict[str, Any]) -> list[str]:
    """
    Produce a compact, human-readable list of drift episodes.
    """
    episodes = temporal.get("episodes", [])

    if not episodes:
        return ["Drift Episodes:", "  (no episodes)"]

    lines = ["Drift Episodes:"]
    for i, ep in enumerate(episodes):
        lines.append(
            f"  Episode {i}: "
            f"windows {ep.get('start_index')}–{ep.get('end_index')}, "
            f"count={ep.get('window_count')}, "
            f"max_drift={ep.get('max_drift')}"
        )

    return lines


def format_window_table(temporal: dict[str, Any]) -> list[str]:
    """
    Produce a compact per-window table (ASCII-style).
    """
    windows = temporal.get("windows", [])

    if not windows:
        return ["Temporal Windows:", "  (no windows)"]

    header = (
        "Temporal Windows:",
        "  idx | admission_ratio | controller_deference_ratio | drift",
        "  ----+------------------+----------------------------+------",
    )

    lines: list[str] = list(header)

    for i, w in enumerate(windows):
        lines.append(
            f"  {i:>3} | "
            f"{_fmt(w.get('admission_ratio')):>16} | "
            f"{_fmt(w.get('controller_deference_ratio')):>26} | "
            f"{_fmt(w.get('drift')):>6}"
        )

    return lines


def join_blocks(*blocks: Iterable[str]) -> str:
    """
    Join multiple formatted blocks into a single string
    suitable for printing.
    """
    out: list[str] = []
    for block in blocks:
        if out:
            out.append("")  # blank line between blocks
        out.extend(block)
    return "\n".join(out)


def _fmt(value: Any) -> str:
    if value is None:
        return "-"
    if isinstance(value, float):
        return f"{value:.3f}"
    return str(value)
