"""
Phase 23 — Canon Intake Pipeline

This pipeline:
- accepts raw user input
- delegates hypothesis generation
- creates belief *candidates* only
- performs NO evaluation
- performs NO mutation outside storage
"""

import time


def run_intake(
    *,
    case_id: str,
    raw_query: str,
    generator,
    controller,
    store,
) -> list[dict]:
    """
    Execute intake for a single query.

    Parameters are keyword-only to prevent accidental misuse.
    """

    # ─────────────────────────────────────────────
    # Controller authorisation (Phase 1–3)
    # ─────────────────────────────────────────────

    if not controller.authorise_intake(case_id, raw_query):
        raise RuntimeError("Intake not authorised by controller")

    # ─────────────────────────────────────────────
    # Hypothesis generation (NON-AUTHORITATIVE)
    # ─────────────────────────────────────────────

    texts = generator.generate(raw_query)

    beliefs: list[dict] = []

    for text in texts:
        belief = {
            "id": controller.new_belief_id(),
            "case_id": case_id,
            "text": text,
            "scope": "assertive",
            "origin": "generator",
            "timestamp": time.time(),
        }
        beliefs.append(belief)

    # ─────────────────────────────────────────────
    # Storage (append-only)
    # ─────────────────────────────────────────────

    store.store_beliefs(case_id, beliefs)

    controller.audit_intake(case_id, raw_query, beliefs)

    return beliefs
