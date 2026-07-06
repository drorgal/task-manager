# task-manager

A simple command-line to-do task manager written in Python. Tasks are persisted to a local `tasks.json` file.

## Requirements

- Python 3.8+ (no external dependencies)

## How to run

```bash
python3 main.py
```

This starts an interactive prompt:

```
To-Do Manager. Type 'help' for commands.
todo> add buy milk
Added task 1.
todo> list
[ ] 1. buy milk
```

## Commands

| Command | Description |
|---|---|
| `add <title>` | Add a new task |
| `list` | Show all tasks |
| `done <id>` | Mark a task as complete |
| `delete <id>` | Delete a task |
| `tag <id> <tag>` | Attach a tag to a task |
| `help` | Show available commands |
| `quit` | Exit (Ctrl+D also works) |

Tasks are saved automatically after every change.
