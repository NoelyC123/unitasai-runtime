from observatory.temporal_correlation import compute_cross_signal_correlation, pearson_r


def test_pearson_r_basic():
    r, n = pearson_r([1.0, 2.0, 3.0], [2.0, 4.0, 6.0])
    assert n == 3
    assert r is not None
    assert r > 0.99


def test_pearson_r_insufficient():
    r, n = pearson_r([1.0], [2.0])
    assert r is None
    assert n == 1


def test_cross_signal_correlation():
    windows = [
        {"admission_ratio": 0.1, "controller_deference_ratio": 0.2},
        {"admission_ratio": 0.2, "controller_deference_ratio": 0.4},
        {"admission_ratio": 0.3, "controller_deference_ratio": 0.6},
    ]
    out = compute_cross_signal_correlation(windows=windows)
    assert out["zero_lag"]["paired_points"] == 3
    assert out["best_abs"] is not None
