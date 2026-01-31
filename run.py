"""
UnitasAI Runtime — Phase 23 Only
"""

from src.intake.intake_pipeline import intake_query
from src.storage.runtime_store import RuntimeStore
from src.controller.runtime_controller import RuntimeController


def main():
    store = RuntimeStore()
    controller = RuntimeController()

    case_id = "demo-case"
    query = input("Enter query: ")

    beliefs = intake_query(case_id, query, store, controller)

    print("\nCandidate beliefs:")
    for b in beliefs:
        print("-", b["text"])


if __name__ == "__main__":
    main()