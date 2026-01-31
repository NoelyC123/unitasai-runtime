"""
Runtime Store (Epistemic Persistence)

Append-only storage.
No mutation.
No inference.
"""

import json
import time
import hashlib
from typing import Any, Dict


class RuntimeStore:
    def __init__(self):
        self._cases = {}

    # ─────────────────────────────────────────────
    # Case management (Phase 1–3 compatible)
    # ─────────────────────────────────────────────

    def create_case(self, case_id: str):
        """
        Canon-compatible alias.
        Explicit case creation.
        """
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

    def store_belief(self, case_id: str, belief: Dict[str, Any]):
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
    # Evaluations (Phase 21B)
    # ─────────────────────────────────────────────

    def store_evaluation(self, case_id: str, evaluation: Any):
        """
        Append-only evaluation artifact.

        Accepts either:
        - dict (preferred, canonical)
        - object with __dict__ (legacy-compatible)

        Stores dict representation only.
        """
        self.ensure_case(case_id)

        if isinstance(evaluation, dict):
            payload = evaluation
        else:
            payload = dict(evaluation.__dict__)

        self._cases[case_id]["evaluations"].append(payload)

        self.log(
            case_id,
            action="EVALUATION",
            payload=payload,
        )

    # ─────────────────────────────────────────────
    # Audit log (append-only)
    # ─────────────────────────────────────────────

    def log(self, case_id: str, action: str, payload: Dict[str, Any]):
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
        """
        Read-only access to audit events.

        This method:
        - Returns existing audit records only
        - Performs no mutation
        - Emits no audit events
        - Does not influence controller behaviour
        - Exists solely for post-hoc observatory analysis
        """
        case = self._cases.get(case_id)
        if not case:
            return []

        return list(case.get("audit", []))