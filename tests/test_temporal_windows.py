"""
Tests for Phase 21B++c — Temporal Authority Drift Windows
"""

from datetime import UTC, datetime, timedelta

from observatory.temporal_windows import compute_temporal_windows


def _ts(offset_seconds: int) -> str:
    base = datetime(2026, 1, 1, 12, 0, 0, tzinfo=UTC)
    return (base + timedelta(seconds=offset_seconds)).isoformat()


def test_empty_events():
    result = compute_temporal_windows([])

    assert result["windows"] == []
    assert result["episodes"] == []
    assert result["metrics"]["window_count"] == 0


def test_two_windows_known_ratios():
    events = [
        # Window 1 (0–300s)
        {
            "timestamp": _ts(10),
            "action": "EVALUATION",
            "payload": {"is_admissible": True},
        },
        {
            "timestamp": _ts(20),
            "action": "EVALUATION",
            "payload": {"is_admissible": False},
        },
        {
            "timestamp": _ts(30),
            "action": "CONTROLLER_DECISION",
            "payload": {"decision": "approved"},
        },
        # Window 2 (300–600s)
        {
            "timestamp": _ts(310),
            "action": "EVALUATION",
            "payload": {"is_admissible": True},
        },
        {
            "timestamp": _ts(320),
            "action": "CONTROLLER_DECISION",
            "payload": {"decision": "rejected"},
        },
        {
            "timestamp": _ts(330),
            "action": "CONTROLLER_DECISION",
            "payload": {"decision": "approved"},
        },
    ]

    result = compute_temporal_windows(events)
    windows = result["windows"]

    assert len(windows) >= 2

    w0 = windows[0]
    w1 = windows[1]

    # Window 1 ratios
    assert w0["evaluation_count"] == 2
    assert w0["admitted_evaluations"] == 1
    assert w0["admission_ratio"] == 0.5

    assert w0["controller_decision_count"] == 1
    assert w0["approved_decisions"] == 1
    assert w0["controller_deference_ratio"] == 1.0

    # Window 2 ratios
    assert w1["evaluation_count"] == 1
    assert w1["admitted_evaluations"] == 1
    assert w1["admission_ratio"] == 1.0

    assert w1["controller_decision_count"] == 2
    assert w1["approved_decisions"] == 1
    assert w1["controller_deference_ratio"] == 0.5

    # Drift sanity
    assert w1["drift"] is not None
    assert w1["drift"] > 0


def test_missing_action_types_handled():
    events = [
        {
            "timestamp": _ts(5),
            "action": "INTAKE",
            "payload": {},
        },
        {
            "timestamp": _ts(15),
            "action": "INTAKE",
            "payload": {},
        },
    ]

    result = compute_temporal_windows(events)
    windows = result["windows"]

    assert len(windows) >= 1
    w = windows[0]

    assert w["evaluation_count"] == 0
    assert w["admission_ratio"] is None
    assert w["controller_decision_count"] == 0
    assert w["controller_deference_ratio"] is None


def test_drift_components_are_exposed():
    events = [
        {
            "timestamp": _ts(10),
            "action": "EVALUATION",
            "payload": {"is_admissible": True},
        },
        {
            "timestamp": _ts(310),
            "action": "EVALUATION",
            "payload": {"is_admissible": False},
        },
    ]

    result = compute_temporal_windows(events)
    windows = result["windows"]

    if len(windows) >= 2:
        w1 = windows[1]
        assert "drift_components" in w1
        comps = w1["drift_components"]
        assert "delta_admission_ratio" in comps
        assert "delta_controller_deference_ratio" in comps
