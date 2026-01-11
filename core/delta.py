"""
YAWN Delta

Tracks changes applied to state over time.
"""

from dataclasses import dataclass, field
from typing import Dict, Any
import time


@dataclass
class Delta:
    timestamp: float = field(default_factory=time.time)
    changes: Dict[str, Any] = field(default_factory=dict)

    def add(self, key: str, value: Any) -> None:
        self.changes[key] = value

    def apply(self, memory: Dict[str, Any]) -> Dict[str, Any]:
        updated = dict(memory)
        updated.update(self.changes)
        return updated

