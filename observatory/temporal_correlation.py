"""
Phase 21B++e — Cross-Signal Temporal Correlation

Read-only. Descriptive only.
No mutation. No authority. No controller influence.

Computes descriptive correlation statistics between:
- admission_ratio
- controller_deference_ratio

Input:
- windows (list of dicts) from Phase 21B++c temporal windows

Output:
- zero-lag Pearson correlation
- lag scan across bounded window offsets
"""

from __future__ import annotations

from math import sqrt
from typing import Any


def compute_cross_signal_correlation(
    *,
    windows: list[dict[str, Any]],
    max_lag_windows: int = 3,
) -> dict[str, Any]:
    a = [_as_float(w.get("admission_ratio")) for w in windows]
    d = [_as_float(w.get("controller_deference_ratio")) for w in windows]

    zero_r, zero_n = pearson_r(a, d)

    lag_rows: list[dict[str, Any]] = []
    best: dict[str, Any] | None = None

    for lag in range(-max_lag_windows, max_lag_windows + 1):
        if lag == 0:
            r, n = zero_r, zero_n
        else:
            aa, dd = _lag_align(a, d, lag)
            r, n = pearson_r(aa, dd)

        row = {"lag": lag, "paired_points": n, "pearson_r": r}
        lag_rows.append(row)

        if r is not None and (best is None or abs(r) > abs(best["pearson_r"])):
            best = row

    return {
        "series": {
            "admission_ratio": a,
            "controller_deference_ratio": d,
        },
        "zero_lag": {
            "paired_points": zero_n,
            "pearson_r": zero_r,
        },
        "lag_scan": lag_rows,
        "best_abs": best,
        "note": "Descriptive statistics only. No causal claims. No prediction. No control influence.",
    }


def pearson_r(
    x: list[float | None],
    y: list[float | None],
) -> tuple[float | None, int]:
    pairs = [(a, b) for a, b in zip(x, y, strict=False) if a is not None and b is not None]
    n = len(pairs)
    if n < 2:
        return None, n

    xs = [p[0] for p in pairs]
    ys = [p[1] for p in pairs]

    mx = sum(xs) / n
    my = sum(ys) / n

    num = sum((xi - mx) * (yi - my) for xi, yi in zip(xs, ys, strict=False))
    denx = sum((xi - mx) ** 2 for xi in xs)
    deny = sum((yi - my) ** 2 for yi in ys)
    den = sqrt(denx * deny)

    if den == 0:
        return None, n

    return num / den, n


def _lag_align(
    a: list[float | None],
    d: list[float | None],
    lag: int,
) -> tuple[list[float | None], list[float | None]]:
    n = min(len(a), len(d))
    a = a[:n]
    d = d[:n]

    if lag > 0:
        return a[: n - lag], d[lag:n]
    if lag < 0:
        k = -lag
        return a[k:n], d[: n - k]
    return a, d


def _as_float(v: Any) -> float | None:
    if v is None:
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None
