# Phase 21B++c — Temporal Authority Drift Windows

## Purpose
Introduce time-windowed analysis of authority drift signals without granting new authority.

This phase adds **temporal aggregation** to RADO outputs only.
It must not:
- influence controller decisions
- mutate beliefs
- alter evaluation admissibility

## Entry Criteria
- Phase 21B advisory evaluation layer is complete
- RADO report generation works end-to-end
- Controller decisions and audit events are persisted with timestamps
- `make check` passes cleanly

## Exit Criteria
- Drift windows can be computed (e.g. last 24h / 7d / 30d)
- Windowed summaries appear in RADO report
- Outputs remain descriptive only
- No new authority paths introduced
- Tests cover window computation logic

## Invariants
- Drift windows may summarise past decisions only
- No belief mutation permitted
- No evaluation override permitted
- No controller influence permitted
- Time windows are observational metadata only

## Explicit Non-Goals
- No alerts
- No thresholds
- No recommendations
- No auto-intervention
- No learning or optimisation

## Canon Alignment
This phase operates entirely outside Canon v0.1 authority paths.
It introduces no new invariants and does not reinterpret existing ones.
