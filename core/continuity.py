"""
YAWN Continuity

Handles resuming execution from existing state.
"""

from typing import Optional

from core.state import YawnState
from storage.base import StorageBackend


class ContinuityManager:
    def __init__(self, storage: StorageBackend):
        self.storage = storage

    def resume(self, state_id: str) -> Optional[YawnState]:
        return self.storage.load(state_id)

    def start(self, state_id: str) -> YawnState:
        state = YawnState(id=state_id)
        self.storage.save(state)
        return state

    def get_or_create(self, state_id: str) -> YawnState:
        existing = self.resume(state_id)
        if existing:
            return existing
        return self.start(state_id)


