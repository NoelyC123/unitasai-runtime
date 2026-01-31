from typing import Protocol, List
from uuid import UUID
from src.models.tension import Tension


class TensionStore(Protocol):
    """
    Canon v0.1 — Tension Store
    Phase: 21C
    """

    def list_by_case(self, case_id: UUID) -> List[Tension]:
        ...

    def insert(self, tension: Tension) -> None:
        ...

    def update(self, tension: Tension) -> None:
        ...
