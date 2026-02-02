from typing import Protocol
from uuid import UUID

from src.models.belief import Belief


class BeliefStore(Protocol):
    """
    Canon v0.1 — Belief Persistent Store Interface
    Phase: 21B / 21C / 21D / 23
    """

    def get(self, belief_id: UUID) -> Belief | None: ...

    def list_by_case(self, case_id: UUID) -> list[Belief]: ...

    def insert(self, belief: Belief) -> None: ...

    def update(self, belief: Belief) -> None: ...
