# UnitasAI — AI Audit Pack (Canon v0.1)

**Purpose**  
This document is a complete, authoritative briefing of all work completed to date on the UnitasAI project.  
It is intended for independent analysis, audit, critique, and stress-testing by AI systems and human reviewers.

This file deliberately separates:
- **What is frozen and binding**
- **What exists but is deferred**
- **What is explicitly prohibited**
- **What has NOT yet been designed**

No assumptions should be made beyond what is written here.

---

## 1. Project Overview

**UnitasAI** is an epistemic reasoning system designed to manage beliefs, justifications, conflicts, revisions, and invariants under strict auditability and minimal-change principles.

The system is explicitly **not**:
- an autonomous decision-maker
- a goal-optimising agent
- a truth oracle
- a self-modifying intelligence

It is a **structured epistemic substrate** intended to support human-aligned reasoning, traceability, and controlled evolution of belief states.

---

## 2. Repository Structure

### 2.1 Canon Repository (Frozen)

**Repo:** `unitasai-canon-v0.1`  
**Status:** FROZEN  
**Tag:** `canon-v0.1`

This repository contains:
- Canonical design specifications
- Phase definitions
- Invariants
- Audit requirements
- Explicit prohibitions
- Reference implementations (structure-only, not performance-optimised)

Nothing in this repository may be modified without a **Canon version bump** (v0.2+).

---

### 2.2 Runtime Repository (Mutable)

**Repo:** `unitasai-runtime`  
**Status:** ACTIVE  
**Purpose:** Execution, experimentation, tooling, UI, CLI, integrations

The Canon is vendored into this repository as **read-only input** under:

```
vendor/unitasai-canon-v0.1/
```

This repo is safe for:
- ChatGPT analysis
- Claude review
- Grok adversarial critique
- Static analysis tools
- Experimental refactors

Canon rules must be respected at all times.

---

## 3. Design Phases — Status Summary

### Completed & Frozen (Canon v0.1)

| Phase | Title | Status |
|------|------|--------|
| 21B | Belief Evaluation Engine | FROZEN |
| 21C | Explicit Conflict & Tension Graphs | FROZEN |
| 21D | Minimal-Change Belief Revision | FROZEN |
| 22 | Invariant Engine (Hard vs Soft) | FROZEN |
| 23 | Epistemic Intake & Evidence Admission | FROZEN |

All underspecified areas in these phases are **recorded but intentionally unresolved**.

---

### Not Yet Designed

| Phase | Description |
|------|-------------|
| 24+ | Temporal reasoning, memory decay, forecasting |
| — | Planning, optimisation, goal systems |
| — | Learning, adaptation, self-modification |

No assumptions should be made about future phases.

---

## 4. Implementation Milestones (IM)

The following **Implementation Milestones (IM)** have been completed and committed in Canon v0.1:

| IM | Description |
|----|------------|
| IM-1 | Artifact & persistent store mapping |
| IM-2 | Canon-aligned repository skeleton |
| IM-3 | Artifact model stubs |
| IM-4 | Persistent store interfaces |
| IM-5 | Controller orchestration interfaces |
| IM-6 | Phase 23 intake pipeline |
| IM-6b | Intake alignment & audit correction |
| IM-7 | Phase 21B evaluation engine |
| IM-8 | Phase 21C tension detection |
| IM-9 | Phase 21D revision enumeration |
| IM-10 | Revision execution controller |
| IM-11 | Phase 22 invariant evaluation |
| IM-12 | Cross-phase invariant safety gates |
| IM-13 | Audit event normalisation |
| IM-14 | Canon integrity guardrails |
| IM-15 | End-to-end dry-run harness |

All IMs are **structure-complete**, not optimisation-complete.

---

## 5. Core Architectural Principles (Binding)

The following principles are **non-negotiable** in Canon v0.1:

1. **Determinism**
   - Given identical stored inputs, outputs must be identical
   - No stochastic or LLM-based logic in evaluators

2. **Append-Only History**
   - Beliefs, evaluations, tensions, revisions are never overwritten
   - State evolution is explicit and auditable

3. **Minimal Change**
   - Revisions must preserve as much of the belief graph as possible

4. **Controller Mediation**
   - Engines never act autonomously
   - Controllers explicitly authorise all state-changing actions

5. **Explicit Non-Actions**
   - If behaviour is not specified, it is prohibited

6. **Audit First**
   - Every meaningful action emits an audit event

---

## 6. What the System Explicitly Does NOT Do

UnitasAI does NOT:
- resolve tensions automatically
- infer truth
- optimise confidence values
- merge beliefs heuristically
- prioritise goals
- learn from outcomes
- act without controller authorisation

Any such behaviour would require Canon v0.2+.

---

## 7. Known Underspecified Areas (Intentionally Deferred)

Canon v0.1 records **40 underspecified areas**, including but not limited to:
- conflict detection mechanics
- invariant predicate language
- confidence update semantics
- temporal reasoning
- duplicate handling rules

These are **not bugs**.  
They are explicit design deferrals.

---

## 8. Audit Guidance for Reviewers (Human or AI)

When reviewing this system, reviewers are encouraged to:

- Identify hidden assumptions
- Look for invariant leakage
- Challenge controller authority boundaries
- Test whether “non-actions” are truly enforced
- Attempt adversarial misuse within Canon constraints

Reviewers must **not**:
- assume missing features are accidental
- propose solutions without version bumping
- collapse uncertainty “for convenience”

---

## 9. Questions This System Is Meant to Support

UnitasAI is designed to help answer questions like:

- *What do we currently believe, and why?*
- *Where are our beliefs in tension?*
- *What is the smallest justified change we can make?*
- *Which constraints were violated, and how severely?*
- *What happened, in what order, and under whose authority?*

---

## 10. Final Note

This project is intentionally conservative, explicit, and slow.

Speed, intelligence amplification, and autonomy are **secondary** to:
- correctness
- traceability
- reversibility
- human oversight

---

**End of AI Audit Pack — Canon v0.1**

