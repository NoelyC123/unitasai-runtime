# Phase 21C — Stability & Recovery Metrics

## Purpose
Measure stability, oscillation, and recovery characteristics of authority drift
over time using existing temporal window outputs.

## Inputs (Existing Only)
- Temporal windows and drift from Phase 21B++c
- Drift threshold already defined in temporal window config

## Metrics (Descriptive)
- Stability index (inverse of drift variance)
- Oscillation count (sign changes in drift deltas)
- Mean recovery windows (time to return below threshold after episode end)
- Worst recovery (max windows to recover)

## Non-Goals
- No alerts
- No thresholds beyond existing drift threshold
- No policy or control
- No mutation or audit emission

## Entry Criteria
- Phase 21B++c, 21B++d, 21B++e complete and frozen
- make check passes

## Exit Criteria
- Helper computes stability/recovery metrics from windows/episodes
- Observatory exposes metrics incrementally
- RADO prints a non-breaking section
- Tests cover metrics
- make check passes

## Invariants
- Read-only
- Case-scoped
- Descriptive only
