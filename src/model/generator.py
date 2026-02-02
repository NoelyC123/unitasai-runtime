"""
Hypothesis Generator (Runtime)

This component:
- generates candidate hypotheses only
- has NO epistemic authority
- does NOT decide truth
- does NOT evaluate invariants
- does NOT mutate state

All authority remains with the RuntimeController.
"""


class HypothesisGenerator:
    """
    Non-authoritative hypothesis generator.

    In production this may wrap:
    - an LLM
    - a rules engine
    - a retrieval system

    For now, it is deterministic and simple.
    """

    def generate(self, raw_query: str) -> list[str]:
        """
        Generate candidate hypotheses.

        This method MUST:
        - return multiple possibilities when possible
        - avoid authoritative language
        - avoid resolution
        """

        raw_query = raw_query.strip()

        if not raw_query:
            return []

        # Demo-only deterministic output
        return [
            f"It is possible that {raw_query}",
            f"One explanation could be that {raw_query}",
        ]
