"""
Runtime Store — Phase 23

Stores candidate beliefs only.
No evaluation, no mutation.
"""

from typing import Dict, List


class RuntimeStore:
    def __init__(self):
        self.cases: Dict[str, Dict[str, List[dict]]] = {}

    def ensure_case(self, case_id: str):
        if case_id not in self.cases:
            self.cases[case_id] = {"candidates": []}

    def record_candidates(self, case_id: str, beliefs: List[dict]):
        self.ensure_case(case_id)
        self.cases[case_id]["candidates"].extend(beliefs)