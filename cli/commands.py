"""
CLI command definitions for YAWN.

Each command maps user intent to core execution logic.
"""

from typing import Optional

from core.continuity import ContinuityManager
from executor.runner import Runner


def run(state_id: str, role: Optional[str] = None) -> None:
    """
    Run YAWN using a given state ID.

    If the state exists, execution resumes.
    If not, a new state is initialized.

    Args:
        state_id: Identifier for the persistent state
        role: Optional execution role to run
    """
    continuity = ContinuityManager(state_id=state_id)
    state = continuity.load_or_create()

    runner = Runner(state=state)

    if role:
        runner.run_role(role)
    else:
        runner.run_all()

    continuity.persist(state)

