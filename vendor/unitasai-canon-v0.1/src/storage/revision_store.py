from typing import Protocol
from uuid import UUID

from src.models.revision_event import RevisionEvent


class RevisionStore(Protocol):
    """
    Canon v0.1 — Revision Event Store
    Phase: 21D
    """

    def list_by_case(self, case_id: UUID) -> list[RevisionEvent]: ...

    def insert(self, revision: RevisionEvent) -> None: ...
