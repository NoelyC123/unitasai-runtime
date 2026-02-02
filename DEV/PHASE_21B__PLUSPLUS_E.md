# Phase 21B++e — Cross-Signal Temporal Correlation

## Purpose
Describe temporal relationships between existing authority-drift signals in a
purely observational manner.

This phase adds correlation and lag analysis over already-computed temporal
windows, without introducing any new authority, inference, or control.

## Signals Used (Existing Only)
- admission_ratio (from EVALUATION.payload.is_admissible)
- controller_deference_ratio (from CONTROLLER_DECISION.payload.decision == "approved")

## Scope (What this phase DOES)
- Compute descriptive correlation statistics between the two ratio series
- Compute zero-lag Pearson correlation
- Compute lagged correlation across a bounded window offset
- Report results via RADO (non-breaking extension)

## Explicit Non-Goals
- No causal claims
- No prediction
- No alerts or thresholds
- No controller interaction
- No RuntimeStore mutation
- No new audit events

## Entry Criteria
- Phase 21B++c complete and frozen
- Phase 21B++d complete
- Temporal windows already computed
- make check passes cleanly

## Exit Criteria (Code-Truth)
- Helper module computes correlation & lag scan from windowed ratios
- AuthorityDriftObservatory exposes a correlation method (incremental)
- RADO prints a correlation section (descriptive only)
- Tests cover correlation logic
- make check passes cleanly

## Invariants
- Case-scoped only
- Read-only
- No authority
- No mutation
- No controller influence

## Authoritative Data Source
The ONLY source of events is:
- store.list_audit_events(case_id)

No alternative access paths.

## Implemented File Inventory (Code Reality)
Created:
- observatory/temporal_correlation.py
- tests/test_temporal_correlation.py

Modified (incremental only):
- observatory/authority_drift.py
- observatory/reports/run_rado.py
