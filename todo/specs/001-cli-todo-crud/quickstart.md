# Quickstart Guide: CLI Todo Application

## Setup

1. Ensure you have Python 3.13 installed
2. Install the project dependencies using `uv`:
   ```bash
   uv venv
   uv pip install -e .
   ```

## Running the Application

To start the CLI application, run:

```bash
cd src
python main.py
```

## Using the Application

Once the application starts, you'll see a prompt where you can enter commands:

### Available Commands

- `add "Title" "Description"` - Add a new task with title and optional description
  Example: `add "Buy groceries" "Milk, eggs, bread"`

- `list` or `ls` - Show all tasks with their status
  Example: `list`

- `update ID "Title" "Description"` - Update the title and/or description of a task
  Example: `update 1 "Updated title" "Updated description"`

- `delete ID` or `del ID` - Remove a task by ID
  Example: `delete 1`

- `done ID` or `toggle ID` - Mark a task as complete/incomplete
  Example: `done 1`

- `help` or `?` - Show available commands
  Example: `help`

## Example Session

```
Welcome to the Todo App!
> add "Buy groceries" "Milk, eggs, bread"
Task added with ID: 1
> add "Call mom"
Task added with ID: 2
> list
1. [ ] Buy groceries - Milk, eggs, bread
2. [ ] Call mom
> done 1
Task 1 marked as complete
> list
1. [x] Buy groceries - Milk, eggs, bread
2. [ ] Call mom
> exit
Goodbye!
```