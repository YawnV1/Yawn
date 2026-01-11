"""
YAWN Roles

Defines logical roles for execution.
"""

from typing import Callable, Dict

from core.state import YawnState


class Role:
    def __init__(self, name: str, fn: Callable[[YawnState], None]):
        self.name = name
        self.fn = fn

    def execute(self, state: YawnState) -> None:
        self.fn(state)


class RoleRegistry:
    def __init__(self):
        self._roles: Dict[str, Role] = {}

    def register(self, role: Role) -> None:
        self._roles[role.name] = role

    def get(self, name: str) -> Role:
        return self._roles[name]

