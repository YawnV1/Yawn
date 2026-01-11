"""
Core primitives for the YAWN execution framework.

This package defines state, continuity, and delta abstractions
used throughout the system.
"""

from .state import State
from .continuity import ContinuityManager
from .delta import Delta

__all__ = [
    "State",
    "ContinuityManager",
    "Delta",
]

