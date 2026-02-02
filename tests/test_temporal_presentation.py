from observatory.presentation.temporal_windows_text import (
    format_drift_episodes,
    format_temporal_summary,
    format_window_table,
    join_blocks,
)


def _sample_temporal():
    return {
        "metrics": {
            "window_count": 3,
            "episode_count": 1,
            "max_drift": 0.5,
            "mean_drift": 0.25,
        },
        "windows": [
            {
                "admission_ratio": 0.5,
                "controller_deference_ratio": 0.8,
                "drift": None,
            },
            {
                "admission_ratio": 0.7,
                "controller_deference_ratio": 0.6,
                "drift": 0.4,
            },
        ],
        "episodes": [
            {
                "start_index": 1,
                "end_index": 1,
                "window_count": 1,
                "max_drift": 0.4,
            }
        ],
    }


def test_format_summary():
    lines = format_temporal_summary(_sample_temporal())
    assert "Window count" in lines[1]
    assert "Episode count" in lines[2]


def test_format_episodes():
    lines = format_drift_episodes(_sample_temporal())
    assert lines[0] == "Drift Episodes:"
    assert "Episode 0" in lines[1]


def test_format_windows():
    lines = format_window_table(_sample_temporal())
    assert lines[0] == "Temporal Windows:"
    assert "admission_ratio" in lines[1]


def test_join_blocks():
    text = join_blocks(["A", "B"], ["C"])
    assert "A" in text
    assert "C" in text
