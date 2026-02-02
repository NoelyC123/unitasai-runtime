from observatory.stability_recovery import compute_stability_and_recovery


def test_stability_and_recovery_basic():
    windows = [
        {"drift": 0.3},
        {"drift": 0.2},
        {"drift": 0.1},
        {"drift": 0.2},
    ]
    episodes = [{"end_index": 0}]
    out = compute_stability_and_recovery(
        windows=windows,
        episodes=episodes,
        drift_threshold=0.25,
    )
    assert out["oscillation_count"] >= 0
    assert out["mean_recovery_windows"] is not None
