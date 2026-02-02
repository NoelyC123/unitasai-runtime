"""
Runtime Store (Epistemic Persistence)

Append-only storage.
No mutation.
No inference.
"""

import json
import time
import hashlib


class RuntimeStore:
    def __init__(self):
        self._cases = {}

    # ─────────────────────────────────────────────
    # Case management
    # ─────────────────────────────────────────────

    def create_case(self, case_id: str):
        self.ensure_case(case_id)

    def ensure_case(self, case_id: str):
        if case_id not in self._cases:
            self._cases[case_id] = {
                "beliefs": [],
                "invariants": [],
                "evaluations": [],
                "audit": [],
            }

    # ─────────────────────────────────────────────
    # Belief storage
    # ─────────────────────────────────────────────

    def store_belief(self, case_id: str, belief: dict):
        self.ensure_case(case_id)
        self._cases[case_id]["beliefs"].append(belief)

    def store_beliefs(self, case_id: str, beliefs: list):
        self.ensure_case(case_id)
        self._cases[case_id]["beliefs"].extend(beliefs)

    def get_beliefs(self, case_id: str):
        self.ensure_case(case_id)
        return list(self._cases[case_id]["beliefs"])

    # ─────────────────────────────────────────────
    # Invariants (stub — Canon v0.1)
    # ─────────────────────────────────────────────

    def get_invariants(self, case_id: str):
        self.ensure_case(case_id)
        return list(self._cases[case_id]["invariants"])

    # ─────────────────────────────────────────────
    # Evaluations (Phase 21B++)
    # ─────────────────────────────────────────────

    def store_evaluation(self, case_id: str, evaluation: dict):
        """
        Append-only evaluation artifact.

        Audit payload is semantically explicit.
        No inference.
        No renaming by observers.
        """
        self.ensure_case(case_id)
        self._cases[case_id]["evaluations"].append(evaluation)

        audit_payload = {
            "belief_id": evaluation["belief_id"],
            "scope": evaluation["scope"],
            "is_admissible": evaluation["is_admissible"],
            "hard_violations": list(evaluation["hard_violations"]),
            "soft_conflicts": list(evaluation["soft_conflicts"]),
        }

        self.log(
            case_id=case_id,
            action="EVALUATION",
            payload=audit_payload,
        )

    # ─────────────────────────────────────────────
    # Audit log (append-only)
    # ─────────────────────────────────────────────

    def log(self, case_id: str, action: str, payload: dict):
        self.ensure_case(case_id)

        entry = {
            "timestamp": time.time(),
            "action": action,
            "payload": payload,
            "hash": hashlib.sha256(
                json.dumps(payload, sort_keys=True).encode()
            ).hexdigest(),
        }

        audit = self._cases[case_id]["audit"]
        if audit:
            entry["prev_hash"] = audit[-1]["hash"]

        audit.append(entry)

    # ─────────────────────────────────────────────
    # Read-only observatory access (RADO)
    # ─────────────────────────────────────────────

    def list_audit_events(self, case_id: str):
        case = self._cases.get(case_id)
        if not case:
            return []
        return list(case["audit"])