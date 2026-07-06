"""JSON persistence for the to-do manager."""

import json
import os


def load(path):
    """Load the task list from disk. Returns an empty list if no file exists."""
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save(path, tasks):
    """Write the task list to disk as JSON."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)
