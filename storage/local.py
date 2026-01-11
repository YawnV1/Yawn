"""
Local Storage Backend for YAWN

Persists state to disk as JSON.
"""

import json
from pathlib import Path
from typing import Optional

from core.state import YawnState


class LocalStorage:
    def __init__(self, root: str = ".yawn"):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def _path(self, state_id: str) -> Path:
        return self.root / f"{state_id}.json"

    def save(self, state: YawnState) -> None:
        path = self._path(state.id)
        with open(path, "w") as f:
            json.dump(state.snapshot(), f, indent=2)

    def load(self, state_id: str) -> Optional[YawnState]:
        path = self._path(state_id)
        if not path.exists():
            return None

        with open(path, "r") as f:
            data = json.load(f)

        return YawnState(
            id=data["id"],
            created_at=data["created_at"],
            updated_at=data["updated_at"],
            memory=data.get("memory", {}),
        )

