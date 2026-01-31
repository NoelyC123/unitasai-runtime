from typing import Protocol, List
from uuid import UUID
from src.models.justification import Justification


class JustificationStore(Protocol):
    """
    Canon v0.1 — Justification Persistent Store Interface
    Phase: 23
    """

    def list_for_belief(self, belief_id: UUID) -> List[Justification]:
        ...

    def insert(self, justification: Justification) -> None:
        ...
