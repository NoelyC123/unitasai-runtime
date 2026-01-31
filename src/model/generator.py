"""
Generator Interface

This module wraps the LLM.
It generates hypotheses ONLY.
It has zero epistemic authority.
"""

from typing import List


def generate_hypotheses(prompt: str) -> List[str]:
    """
    Return a list of neutral, conditional hypotheses.

    This is a stub.
    LLM wiring happens later.
    """
    return [
        f"It is possible that {prompt}",
        f"One explanation could be that {prompt}",
    ]