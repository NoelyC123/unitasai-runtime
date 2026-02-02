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

### Phase 21B++b — Advisory Evaluation Layer
Status: COMPLETE

### Phase 21B++c — Temporal Authority Drift Windows
Status: COMPLETE

### Phase 21B++d — Drift Presentation & Summarisation
Status: COMPLETE

### Phase 21B++e — Cross-Signal Temporal Correlation
Status: COMPLETE

---

## Phase 21C — Stability & Recovery Metrics
Status: COMPLETE

Purpose:
- Measure system stability over time
- Detect oscillation and recovery patterns

Notes:
- Observational only
- Builds on Phase 21B outputs

---

## Phase 22 — Epistemic Health Index (EHI)
Status: COMPLETE

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
