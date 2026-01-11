"""
Claude Adapter for YAWN

Abstracts interaction with Claude.
"""

from typing import Dict, Any

from core.state import YawnState


class ClaudeExecutor:
    def __init__(self, model: str = "claude-3"):
        self.model = model

    def plan(self, state: YawnState) -> Dict[str, Any]:
        """
        Given current state, produce a plan or output.
        Stubbed for now.
        """
        return {
            "status": "noop",
            "memory_keys": list(state.memory.keys()),
        }

