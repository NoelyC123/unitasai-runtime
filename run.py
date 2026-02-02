"""
UnitasAI Runtime Entry Point
"""

from src.storage.runtime_store import RuntimeStore
from src.controller.runtime_controller import RuntimeController
from src.intake.intake_pipeline import run_intake
from src.intake.generators.simple_generator import SimpleBeliefGenerator
from src.evaluation.evaluation_engine import run_evaluation
from observatory.reports.run_rado import run_rado


GLOBAL_RUNTIME_STORE = RuntimeStore()


def main():
    controller = RuntimeController(store=GLOBAL_RUNTIME_STORE)
    generator = SimpleBeliefGenerator()

    case_id = "demo-case"

    query = input("Enter query:\n> ").strip()

    # ─────────────────────────────────────────────
    # Intake
    # ─────────────────────────────────────────────

    beliefs = run_intake(
        case_id=case_id,
        raw_query=query,
        generator=generator,
        controller=controller,
        store=GLOBAL_RUNTIME_STORE,
    )

    print("\nCandidate beliefs:")
    for b in beliefs:
        print(f"- {b['text']}")

    # ─────────────────────────────────────────────
    # Evaluation
    # ─────────────────────────────────────────────

    evaluations = run_evaluation(
        case_id=case_id,
        beliefs=beliefs,
        controller=controller,
        store=GLOBAL_RUNTIME_STORE,
    )

    print("\nEvaluation results:")
    for e in evaluations:
        print(
            f"- belief_id: {e['belief_id']} | "
            f"scope: {e['scope']} | "
            f"is_admissible: {e['is_admissible']} | "
            f"hard violations: {e['hard_violations']} | "
            f"soft conflicts: {e['soft_conflicts']}"
        )

    # ─────────────────────────────────────────────
    # RADO (post-hoc, read-only)
    # ─────────────────────────────────────────────

    run_rado(
        store=GLOBAL_RUNTIME_STORE,
        case_id=case_id,
    )


if __name__ == "__main__":
    main()