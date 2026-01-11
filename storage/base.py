"""
Storage Base Interface for YAWN

Defines the contract all storage backends must follow.
"""

from abc import ABC, abstractmethod
from typing import Optional

from core.state import YawnState


class StorageBackend(ABC):
    @abstractmethod
    def save(self, state: YawnState) -> None:
        """Persist a YawnState."""
        raise NotImplementedError

    @abstractmethod
    def load(self, state_id: str) -> Optional[YawnState]:
        """Load a YawnState by ID."""
        raise NotImplementedError

