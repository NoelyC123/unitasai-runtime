from dataclasses import dataclass

from src.storage.audit_store import AuditStore
from src.storage.belief_store import BeliefStore
from src.storage.evaluation_store import EvaluationStore
from src.storage.invariant_store import InvariantStore
from src.storage.justification_store import JustificationStore
from src.storage.revision_store import RevisionStore
from src.storage.tension_store import TensionStore


@dataclass(frozen=True)
class ControllerContext:
    """
    Canon v0.1 — Controller Dependency Context

    HARD RULES:
    - No defaults
    - No lazy wiring
    - No optional stores
    - No mutation
    """

    belief_store: BeliefStore
    justification_store: JustificationStore
    evaluation_store: EvaluationStore
    tension_store: TensionStore
    revision_store: RevisionStore
    invariant_store: InvariantStore
    audit_store: AuditStore
