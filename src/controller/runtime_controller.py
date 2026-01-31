"""
Runtime Controller

The ONLY authority-bearing component.
"""

import uuid
import time


class RuntimeController:
    def authorise_intake(self, case_id: str, raw_query: str):
        # Placeholder for future policy checks
        return True

    def new_belief_id(self) -> str:
        return str(uuid.uuid4())

    def audit_intake(self, case_id: str, raw_query: str, beliefs: list):
        # Phase 23 audit stub
        print(
            f"[AUDIT] {time.time()} — Intake for case {case_id}: "
            f"{len(beliefs)} candidate beliefs"
        )