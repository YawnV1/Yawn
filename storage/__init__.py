"""
Persistence layer for YAWN.

Defines storage backend interfaces and concrete implementations
used to persist execution state.
"""

from .base import StorageBackend
from .local import LocalStorage

__all__ = [
    "StorageBackend",
    "LocalStorage",
]

