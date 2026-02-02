from typing import Protocol
from uuid import UUID

from src.models.invariant import Invariant


class InvariantStore(Protocol):
    """
    Canon v0.1 — Invariant Store
    Phase: 22
    """

    def list_active(self, case_id: UUID) -> list[Invariant]: ...

    def insert(self, invariant: Invariant) -> None: ...
