# IM-1 — Canon Artifact & Persistent Store Mapping
Canon Version: v0.1
Status: LOCKED (implementation reference)
Authority: Authoritative System Memory v0.1

---

## PURPOSE

This document defines:
1. All first-class epistemic artifacts mandated by Canon v0.1
2. Which artifacts MUST be persisted
3. Which artifacts are append-only
4. Which artifacts are mutable only via governed engines

No implementation may introduce or remove artifacts not listed here
without a Canon version bump.

---

## SECTION A — FIRST-CLASS EPISTEMIC ARTIFACTS

### A1. Belief
- Identity: belief_id (UUID, immutable)
- Persisted: YES
- Mutable fields: status, confidence, scope (Phase 21D only)
- Immutable fields: text, case_id, created_at
- Created via: Phase 23 Intake
- Never deleted

### A2. Justification
- Identity: justification_id (UUID, immutable)
- Persisted: YES
- Immutable content
- May be withdrawn (status only, if implemented)
- Created via: Phase 23 Intake
- Never deleted

### A3. Tension
- Identity: tension_id (UUID, immutable)
- Persisted: YES
- Append-only lifecycle
- Resolved/superseded only via governed processes
- Created via: Phase 21C

### A4. EvaluationResult
- Identity: evaluation_id (UUID, immutable)
- Persisted: YES
- Append-only
- Advisory only
- Created via: Phase 21B

### A5. RevisionEvent
- Identity: revision_id (UUID, immutable)
- Persisted: YES
- Append-only
- Records belief state transitions
- Created via: Phase 21D

### A6. Invariant
- Identity: invariant_id (UUID, immutable)
- Persisted: YES
- Strength immutable (hard/soft)
- Status lifecycle: active / suspended / retired
- Created via: Phase 22

### A7. IntakeRequest
- Identity: request_id (UUID, immutable)
- Persisted: OPTIONAL (audit required regardless)
- Never modifies epistemic state directly
- Created via: Phase 23

### A8. AuditEvent
- Identity: audit_event_id (UUID or equivalent)
- Persisted: YES
- Append-only
- Global forensic record
- Cannot be modified or deleted

---

## SECTION B — PERSISTENT STORES (REQUIRED)

### B1. Beliefs Store
- Table: beliefs
- Persistence: REQUIRED
- Deletion: PROHIBITED

### B2. Justifications Store
- Table: justifications
- Persistence: REQUIRED
- Deletion: PROHIBITED

### B3. Tensions Store
- Table: tensions
- Persistence: REQUIRED
- Deletion: PROHIBITED

### B4. Evaluations Store
- Table: evaluations
- Persistence: REQUIRED
- Append-only

### B5. Revisions Store
- Table: revisions
- Persistence: REQUIRED
- Append-only

### B6. Invariants Store
- Table: invariants
- Persistence: REQUIRED
- Never deleted

### B7. Audit Store
- Table: audit_log
- Persistence: REQUIRED
- Append-only
- System-wide

---

## SECTION C — NON-PERSISTENT / COMPUTED ARTIFACTS

The following are explicitly NON-persistent:
- Conflict previews
- Tension previews
- Hypothetical belief states
- Pre-check results
- Candidate revision enumerations
- Evaluation computation intermediates

---

## SECTION D — GOVERNANCE GUARANTEES

1. No artifact may be deleted unless Canon explicitly permits it
2. No artifact may be modified outside its governing phase
3. All persisted artifacts must be reconstructible via audit
4. Underspecified areas remain unresolved by implementation
5. Any deviation requires Canon v0.2+

---

## IM-1 STATUS

IM-1 COMPLETE.
This document is the authoritative bridge between Canon v0.1 and code.
