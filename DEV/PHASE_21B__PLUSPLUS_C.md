# Phase 21B++c — Temporal Authority Drift Windows

## Purpose
Introduce time-windowed analysis of *existing* authority-drift signals without granting new authority.

This phase adds **temporal aggregation** to **RADO outputs only**.
It must not:
- influence controller decisions
- mutate beliefs
- alter evaluation admissibility

## Scope (What this phase DOES)
Compute fixed time windows over **case-scoped audit events** and derive descriptive:
- per-window `admission_ratio` from `EVALUATION` events (`payload.is_admissible`)
- per-window `controller_deference_ratio` from `CONTROLLER_DECISION` events (`payload.decision == "approved"`)
- window-to-window drift: `|Δ admission_ratio| + |Δ controller_deference_ratio|`
- drift episodes: contiguous windows where `drift > drift_threshold`

## Entry Criteria
- Phase 21B advisory evaluation layer is complete
- RADO report generation works end-to-end
- Controller decisions and audit events are persisted with timestamps
- `make check` passes cleanly

## Exit Criteria (Code-Truth)
- A helper module computes windows + drift + episodes from `audit_events`
- RADO prints an additional section for temporal windows (non-breaking)
- Outputs remain descriptive only
- No new authority paths introduced
- Tests cover window computation logic
- `make check` passes cleanly

## Invariants
- Drift windows may summarise past decisions only
- No belief mutation permitted
- No evaluation override permitted
- No controller influence permitted
- Time windows are observational metadata only

## Explicit Non-Goals
- No alerts
- No recommendations
- No auto-intervention
- No learning or optimisation
- No cross-case comparisons

## Canon Alignment
This phase operates entirely outside Canon v0.1 authority paths.
It introduces no new invariants and does not reinterpret existing ones.

## Authoritative Data Source
The ONLY source of events for this phase is:
- `store.list_audit_events(case_id)`

No alternative store accessors. No new event schema requirements.

## Implemented File Inventory (Code Reality)
Created:
- `observatory/temporal_windows.py`
- `tests/test_temporal_windows.py`
- `tests/conftest.py`

Modified (incremental extension only):
- `observatory/authority_drift.py` (adds `temporal_authority_drift_windows(...)` method)
- `observatory/reports/run_rado.py` (prints temporal windows section; does not remove existing output)

## Metrics (Code Reality)
Per-window:
- `evaluation_count`
- `admitted_evaluations`
- `admission_ratio = admitted_evaluations / evaluation_count` (or `None` if zero)
- `controller_decision_count`
- `approved_decisions`
- `controller_deference_ratio = approved_decisions / controller_decision_count` (or `None` if zero)

Window-to-window:
- `drift = |Δ admission_ratio| + |Δ controller_deference_ratio|`
- `drift_components`: `delta_admission_ratio`, `delta_controller_deference_ratio`

Episodes:
- contiguous windows where `drift > drift_threshold`

Summary:
- `window_count`, `episode_count`, `max_drift`, `mean_drift`

## Notes
- All outputs are descriptive only.
- No mutation of RuntimeStore.
- No audit emission from observatory paths.
