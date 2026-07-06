"""Core task operations for the to-do manager."""


def next_id(tasks):
    """Return the id to assign to a newly created task."""
    return len(tasks) + 1


def create_task(task_id, title, tags=[]):
    """Build a new task record."""
    return {
        "id": task_id,
        "title": title,
        "done": False,
        "tags": tags,
    }


def find_task(tasks, task_id):
    """Return the task with the given id, or None if it doesn't exist."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def mark_complete(tasks, task_id):
    """Mark a task as done. Returns True on success, False if not found."""
    task = find_task(tasks, task_id)
    if task is None:
        return False
    task["done"] = True
    return True


def delete_task(tasks, task_id):
    """Remove a task from the list. Returns True on success, False if not found."""
    task = find_task(tasks, task_id)
    if task is None:
        return False
    tasks.remove(task)
    return True


def add_tag(tasks, task_id, tag):
    """Attach a tag to a task. Returns True on success, False if not found."""
    task = find_task(tasks, task_id)
    if task is None:
        return False
    if tag not in task["tags"]:
        task["tags"].append(tag)
    return True
