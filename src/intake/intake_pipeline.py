"""
Phase 23 — Epistemic Intake Pipeline

This module is responsible for:
- Accepting raw user input
- Invoking the generator
- Emitting candidate belief objects
- Recording audit events

It MUST NOT:
- Evaluate beliefs
- Assign confidence
- Enforce invariants
- Resolve tensions
- Mutate existing beliefs
"""

from typing import List, Dict, Any
from src.model.generator import generate_hypotheses
from src.storage.runtime_store import RuntimeStore
from src.controller.runtime_controller import RuntimeController


def intake_query(
    case_id: str,
    raw_query: str,
    store: RuntimeStore,
    controller: RuntimeController,
) -> List[Dict[str, Any]]:
    """
    Intake a raw query and return candidate belief objects.

    All authority remains with the controller.
    """

    controller.authorise_intake(case_id, raw_query)

    hypotheses = generate_hypotheses(raw_query)

    beliefs = []
    for h in hypotheses:
        belief = {
            "id": controller.new_belief_id(),
            "text": h,
            "status": "candidate",
            "scope": "assertive",
            "origin": "generator",
        }
        beliefs.append(belief)

    store.record_candidates(case_id, beliefs)
    controller.audit_intake(case_id, raw_query, beliefs)

    return beliefs