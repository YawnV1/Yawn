"""
YAWN Runner

Coordinates state, execution, and persistence.
"""

from typing import Callable

from core.state import YawnState
from storage.base import StorageBackend


class Runner:
    def __init__(self, storage: StorageBackend):
        self.storage = storage

    def run(self, state: YawnState, fn: Callable[[YawnState], None]) -> YawnState:
        """
        Execute a function against state and persist the result.
        """
        fn(state)
        self.storage.save(state)
        return state

