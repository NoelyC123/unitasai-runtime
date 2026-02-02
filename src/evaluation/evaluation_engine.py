"""
Evaluation Engine — Phase 21B

Deterministic.
Non-authoritative.
"""


def run_evaluation(*, case_id, beliefs, controller, store):
    evaluations = []

    for belief in beliefs:
        evaluation = {
            "belief_id": belief["id"],
            "scope": belief["scope"],
            "is_admissible": True,
            "hard_violations": [],
            "soft_conflicts": [],
        }

        # Store evaluation (append-only)
        store.store_evaluation(case_id, evaluation)

        # ─────────────────────────────────────────
        # Explicit controller decision
        # ─────────────────────────────────────────
        controller.decide_evaluation(
            case_id=case_id,
            evaluation=evaluation,
        )

        evaluations.append(evaluation)

    return evaluations
