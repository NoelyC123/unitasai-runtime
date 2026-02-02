from observatory.epistemic_health import compute_epistemic_health_index


def test_epistemic_health_index_minimal():
    temporal = {
        "windows": [{"drift": 0.1}, {"drift": 0.2}],
        "episodes": [],
    }
    correlation = {
        "zero_lag": {"pearson_r": 0.3},
        "best_abs": {"pearson_r": 0.3, "lag": 0},
    }
    stability = {
        "stability_index": 10.0,
        "oscillation_count": 1,
        "mean_recovery_windows": None,
        "max_recovery_windows": None,
    }

    out = compute_epistemic_health_index(
        temporal=temporal,
        correlation=correlation,
        stability=stability,
    )

    assert "drift_health" in out
    assert "stability_health" in out
    assert "alignment_health" in out
