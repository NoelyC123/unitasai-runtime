# UnitasAI Canon v0.1 — Master Index (Authoritative)

**Canon Version**: v0.1  
**Status**: FROZEN (no modifications without version bump)  
**Tag**: canon-v0.1  
**Repo**: unitasai-canon-v0.1 (GitHub)  

---

## 0) What This Document Is

This file is the single authoritative “table of contents + briefing pack” for Canon v0.1.

It exists to ensure:
- No knowledge is lost across tools or assistants
- Canon constraints remain stable and enforceable
- Implementation work can be audited for compliance

---

## 1) Canon Lock Declaration

Canon v0.1 is locked and may not be modified except by explicit version bump:
- Canon v0.2, v0.3, etc. require:
  1) explicit bump
  2) change rationale
  3) impact assessment
  4) audit trail

**Rule**: Implementations may vary internally, but MUST satisfy Canon constraints.

---

## 2) Canon Phases Included (Frozen)

### Phase 21B — Belief Evaluation Engine (FROZEN)
- Purpose: Evaluate beliefs in a case; non-authoritative; read-only inputs; emits evaluation results.
- Boundaries: Evaluator does not enforce invariants; it reads context only.

### Phase 21C — Explicit Conflict & Tension Graphs (FROZEN)
- Purpose: Detect and represent explicit tensions between beliefs.
- Boundaries: Tension engine is non-resolving; controller authorises tension creation.

### Phase 21D — Minimal-Change Belief Revision Engine (FROZEN)
- Purpose: Enumerate and execute minimal-change revisions, controller-mediated.
- Boundaries: Revision changes beliefs to satisfy constraints; does not change invariants.

### Phase 22 — Invariant Engine (Hard vs Soft Constraints) (FROZEN)
- Purpose: Mechanistic constraints over belief states. Hard blocks; soft warns/tensions.
- Boundaries: Invariant engine detects + blocks (hard) but does not modify beliefs.

### Phase 23 — Epistemic Event & Evidence Intake (FROZEN)
- Purpose: Single entry path for new beliefs + justifications.
- Boundaries: Intake is controller-mediated; content immutable post-admission.

---

## 3) Canon Artifacts (Schemas / First-Class Objects)

This section lists the canonical artifacts and their key identity guarantees.

- Belief
- Justification
- EvaluationResult
- Tension
- RevisionEvent
- Invariant
- AuditEvent
- Intake Requests (BeliefIntakeRequest, JustificationIntakeRequest)

(See src/models/* for structure stubs in implementation mapping.)

---

## 4) Canon Persistent Stores (Interfaces / Backing Data)

This section lists the persistent stores required by Canon.

- BeliefStore
- JustificationStore
- EvaluationStore
- TensionStore
- RevisionStore
- InvariantStore
- AuditStore

(See src/storage/* for interface stubs in implementation mapping.)

---

## 5) Implementation Mapping (IM) — Completed Work

This section maps the Canon to implemented repository scaffolding.

### IM-1 — Artifact & Persistent Store Mapping
- File: canon/IM-1_ARTIFACTS_AND_PERSISTENT_STORES.md

### IM-2 — Canon-aligned repository skeleton and boundary scaffolding
- Added: src/ module tree + README boundaries

### IM-3 — Canon artifact model stubs (structure only)
- Added: src/models/*.py

### IM-4 — Persistent store interfaces (schema-level)
- Added: src/storage/*.py

### IM-5 — Controller orchestration interfaces
- Added: src/controller/*.py (context + controllers)

### IM-6 / IM-6b — Intake engine wiring (Phase 23)
- Added: src/intake/*

### IM-7 — Evaluation engine + controller (Phase 21B)
- Added: src/evaluation/*

### IM-8 — Tension engine + controller (Phase 21C)
- Added: src/tensions/*

### IM-9 — Revision enumeration engine (Phase 21D)
- Added: src/revision/revision_engine.py

### IM-10 — Revision execution + audit (Phase 21D)
- Added: src/revision/revision_executor.py

### IM-11 — Invariant evaluation engine (Phase 22, non-enforcing)
- Added: src/invariants/*

### IM-12 — Cross-phase invariant safety gates (intake + revision)
- Updated: controller orchestration to respect hard invariant blocking

### IM-13 — Audit event normalisation and completeness
- Updated: audit model/store/controller alignment

### IM-14 — Canon integrity guardrails and forbidden-path enforcement
- Added: src/utils/canon_guards.py

### IM-15 — Canon v0.1 end-to-end dry-run harness
- Added: src/utils/dry_run_harness.py

---

## 6) Underspecified Areas Registry (Frozen as Recorded)

Canon v0.1 includes deferred items across phases that MUST NOT be silently resolved.
They may only be resolved via Canon v0.2+.

- Phase 21C: 10 deferred
- Phase 21D: 10 deferred
- Phase 22: 10 deferred
- Phase 23: 10 deferred
**Total**: 40 deferred items

(Reference: CANON_STATUS.md)

---

## 7) AI Usage Rules (Operational)

### Allowed:
- Implementation choices inside constraints
- Additional logging (non-authoritative)
- Defensive checks that do not alter semantics

### Forbidden:
- Editing frozen specs without version bump
- LLM-dependent predicate evaluation
- Auto-resolution of deferred items
- Cross-case contamination
- Silent bypass of audits

---

## 8) Current Repo State (Snapshot Fields)

- Repo root: unitasai_canon_v0_1
- Branches: main, canon-v0.1-frozen
- Tag: canon-v0.1
- Status file: CANON_STATUS.md
- Master index: CANON_INDEX.md (this file)

---

## 9) Next Steps Roadmap (Non-Canon)

1) Create runtime repo: unitasai-runtime (separate from Canon)
2) Vendor canon/v0.1 into runtime (read-only mirror)
3) Add AI briefing packs (ChatGPT / Claude / Grok)
4) Run structured audits using each AI on the snapshot bundle
