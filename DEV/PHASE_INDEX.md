# UnitasAI — Development Phase Index (Authoritative)

This file is the single source of truth for UnitasAI development phases.

All agents, chats, and contributors MUST:
- Treat this file as canonical
- Follow phases in order
- Respect phase invariants and non-goals
- Avoid skipping, merging, or redefining phases

No phase may be considered complete unless:
- Its exit criteria are met
- `make check` passes
- The phase file exists under DEV/

---

## Rules of Engagement (Global)

Applies to ALL phases below.

- Canon v0.1 is locked unless explicitly stated otherwise
- RuntimeStore is authoritative
- Observatory layers are read-only
- No mutation unless a phase explicitly authorises it
- No refactors unless explicitly authorised
- Incremental extensions only
- Full-file edits only (no partial snippets)
- `make check` must pass after every logical step

---

## Phase 21B — Advisory & Observability Track

### Phase 21B++a — Audit Semantic Normalisation
Status: COMPLETE
Purpose: Ensure audit events are semantically consistent and machine-readable.
Notes: No control logic, no mutation.

---

### Phase 21B++b — Advisory Evaluation Layer
Status: COMPLETE
Purpose: Introduce advisory-only evaluation signals without authority.
Notes: Evaluator remains non-binding.

---

### Phase 21B++c — Temporal Authority Drift Windows
Status: COMPLETE
Spec File: `DEV/PHASE_21B__PLUSPLUS_C.md`

Purpose:
- Add time-windowed observability to existing authority drift signals.

Key Guarantees:
- No new authority
- No mutation
- Case-scoped only
- Descriptive metrics only

Implemented:
- Fixed time windows
- Per-window ratios
- Window-to-window drift
- Drift episodes
- RADO non-breaking extension
- Full test coverage

---

### Phase 21B++d — Drift Presentation & Summarisation
Status: NOT STARTED

Purpose:
- Improve human interpretability of drift data
- Presentation only (no new computation)

Allowed:
- Aggregated summaries (counts, durations)
- Textual timelines (ASCII / tables)
- CLI-friendly formatting options

Explicitly Forbidden:
- Threshold-based decisions
- Alerts
- Policy recommendations
- Controller interaction

---

### Phase 21B++e — Cross-Signal Temporal Correlation
Status: NOT STARTED

Purpose:
- Describe temporal relationships between existing signals
- Example: admission drift vs controller deference drift

Allowed:
- Correlation coefficients
- Lag analysis
- Descriptive statistics

Forbidden:
- Causal claims
- Predictive modelling
- Control influence

---

## Phase 21C — Stability & Recovery Metrics
Status: NOT STARTED

Purpose:
- Measure system stability over time
- Detect oscillation and recovery patterns

Notes:
- Observational only
- Builds on Phase 21B outputs

---

## Phase 22 — Epistemic Health Index (EHI)
Status: NOT STARTED

Purpose:
- Aggregate long-term observability metrics
- Produce a descriptive system health profile

Notes:
- No gating
- No scoring thresholds
- No decisions

---

## Phase 23 — Governance & Audit Export
Status: NOT STARTED

Purpose:
- External auditability
- Legal / regulatory defensibility

Outputs:
- JSON
- CSV
- Signed bundles

---

## End of Index

Any phase not listed here MUST NOT be implemented.
Any deviation requires an explicit update to this file.
