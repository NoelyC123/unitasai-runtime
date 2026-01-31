from typing import Protocol, List
from uuid import UUID
from src.models.invariant import Invariant


class InvariantStore(Protocol):
    """
    Canon v0.1 — Invariant Store
    Phase: 22
    """

    def list_active(self, case_id: UUID) -> List[Invariant]:
        ...

    def insert(self, invariant: Invariant) -> None:
        ...
