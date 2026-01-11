"""
YAWN CLI Entry Point
"""

import sys

from core.continuity import ContinuityManager
from executor.runner import Runner
from storage.local import LocalStorage


def main():
    if len(sys.argv) < 3:
        print("usage: yawn run <state_id>")
        sys.exit(1)

    command = sys.argv[1]
    state_id = sys.argv[2]

    storage = LocalStorage()
    continuity = ContinuityManager(storage)
    runner = Runner(storage)

    state = continuity.get_or_create(state_id)

    if command == "run":
        def noop(s):
            s.set("last_run", "ok")

        runner.run(state, noop)
        print(f"YAWN state '{state_id}' updated.")
    else:
        print(f"unknown command: {command}")


if __name__ == "__main__":
    main()

