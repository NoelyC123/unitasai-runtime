"""
SimpleBeliefGenerator (Canon v0.1)

Non-authoritative hypothesis generator.

This generator:
- Produces raw textual hypotheses only
- Performs no validation
- Performs no inference
- Assigns no IDs
- Assigns no metadata
- Exists solely to externalise candidate text generation
"""

from typing import List


class SimpleBeliefGenerator:
    """
    Minimal hypothesis generator.

    Canon constraints:
    - No epistemic authority
    - No belief shaping
    - Deterministic given identical input
    """

    def generate(self, raw_query: str) -> List[str]:
        """
        Return raw hypothesis strings only.
        """
        return [
            raw_query
        ]