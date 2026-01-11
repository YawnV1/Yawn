"""
YAWN State

This module defines the persistent state model for YAWN.
State is deliberately simple, serializable, and model-agnostic.
"""

from dataclasses import dataclass, field
from typing import Dict, Any
import time


@dataclass
class YawnState:
    """
    Represents long-lived state across executions.
    This is NOT conversation history.
    """

    id: str
    created_at: float = field(default_factory=time.time)
    updated_at: float = field(default_factory=time.time)

    # Arbitrary persistent memory
    memory: Dict[str, Any] = field(default_factory=dict)

    def touch(self) -> None:
        """Update the last-modified timestamp."""
        self.updated_at = time.time()

    def set(self, key: str, value: Any) -> None:
        """Set a memory value."""
        self.memory[key] = value
        self.touch()

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a memory value."""
        return self.memory.get(key, default)

    def snapshot(self) -> Dict[str, Any]:
        """
        Return a serializable snapshot of the state.
        """
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "memory": self.memory,
        }

