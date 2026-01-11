"""
Execution layer for YAWN.

This package contains role definitions, execution runners,
and orchestration logic.
"""

from .runner import Runner
from .roles import RoleRegistry

__all__ = [
    "Runner",
    "RoleRegistry",
]

