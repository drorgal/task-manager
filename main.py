"""Interactive command-line to-do task manager."""

import storage
import tasks

DATA_FILE = "tasks.json"

HELP = """Commands:
  add <title>       Add a new task
  list              Show all tasks
  done <id>         Mark a task as complete
  delete <id>       Delete a task
  tag <id> <tag>    Attach a tag to a task
  help              Show this message
  quit              Exit"""


def print_tasks(todos):
    if not todos:
        print("No tasks yet.")
        return
    for task in todos:
        status = "x" if task["done"] else " "
        line = "[" + status + "] " + task["id"] + ". " + task["title"]
        if task["tags"]:
            line += "  (" + ", ".join(task["tags"]) + ")"
        print(line)


def parse_id(value):
    try:
        return int(value)
    except ValueError:
        return None


def main():
    todos = storage.load(DATA_FILE)
    print("To-Do Manager. Type 'help' for commands.")

    while True:
        try:
            raw = input("todo> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not raw:
            continue

        command, _, arg = raw.partition(" ")
        arg = arg.strip()

        if command == "add":
            if not arg:
                print("Usage: add <title>")
                continue
            task = tasks.create_task(tasks.next_id(todos), arg)
            todos.append(task)
            storage.save(DATA_FILE, todos)
            print(f"Added task {task['id']}.")

        elif command == "list":
            print_tasks(todos)

        elif command == "done":
            task_id = parse_id(arg)
            if task_id is None:
                print("Usage: done <id>")
                continue
            if tasks.mark_complete(todos, task_id):
                storage.save(DATA_FILE, todos)
                print(f"Task {task_id} completed.")
            else:
                print(f"No task with id {task_id}.")

        elif command == "delete":
            task_id = parse_id(arg)
            if task_id is None:
                print("Usage: delete <id>")
                continue
            if tasks.delete_task(todos, task_id):
                storage.save(DATA_FILE, todos)
                print(f"Task {task_id} deleted.")
            else:
                print(f"No task with id {task_id}.")

        elif command == "tag":
            id_part, _, tag = arg.partition(" ")
            task_id = parse_id(id_part)
            tag = tag.strip()
            if task_id is None or not tag:
                print("Usage: tag <id> <tag>")
                continue
            if tasks.add_tag(todos, task_id, tag):
                storage.save(DATA_FILE, todos)
                print(f"Tagged task {task_id} with '{tag}'.")
            else:
                print(f"No task with id {task_id}.")

        elif command == "help":
            print(HELP)

        elif command in ("quit", "exit"):
            break

        else:
            print(f"Unknown command: {command}. Type 'help' for commands.")

    print("Bye.")


if __name__ == "__main__":
    main()
