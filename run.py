"""
Runtime CLI — Demonstration Harness

NOT Canon.
Used only to exercise the runtime pipeline safely.
"""

from src.model.generator import HypothesisGenerator
from src.controller.runtime_controller import RuntimeController
from src.storage.runtime_store import RuntimeStore
from src.intake.intake_pipeline import run_intake


def main():
    case_id = "demo-case"

    store = RuntimeStore()
    controller = RuntimeController()
    generator = HypothesisGenerator()

    store.create_case(case_id)

    raw_query = input("Enter query:\n> ").strip()
    if not raw_query:
        print("No input provided.")
        return

    # ─────────────────────────────────────────────
    # Phase 23 — Intake
    # ─────────────────────────────────────────────

    beliefs = run_intake(
        case_id=case_id,
        raw_query=raw_query,
        generator=generator,
        controller=controller,
        store=store,
    )

    print("\nCandidate beliefs:")
    for b in beliefs:
        print("-", b["text"])

    # ─────────────────────────────────────────────
    # Phase 21B — Evaluation
    # ─────────────────────────────────────────────

    evaluations = controller.evaluate_beliefs(
        case_id=case_id,
        beliefs=beliefs,
        invariants=store.get_invariants(case_id),
    )

    for e in evaluations:
        store.store_evaluation(case_id, e)

    print("\nEvaluation results:")
    for e in evaluations:
        print(
            "- belief_id:", e.belief_id,
            "| scope:", e.scope,
            "| admissible:", e.admissible,
            "| hard violations:", e.hard_violations,
            "| soft conflicts:", e.soft_conflicts,
        )


if __name__ == "__main__":
    main()