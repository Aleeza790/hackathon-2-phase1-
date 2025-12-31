# Data Model: CLI Todo Application

## Entities

### Task
The core entity representing a todo item in the system.

**Attributes:**
- `id` (int): Unique identifier for the task, auto-incremented starting from 1
- `title` (str): Required title of the task, cannot be empty
- `description` (str | None): Optional description of the task, defaults to None
- `completed` (bool): Boolean indicating whether the task is completed, defaults to False

**Validation Rules:**
- `id` must be unique across all tasks
- `id` must be a positive integer
- `title` cannot be empty or None
- `completed` must be a boolean value

**State Transitions:**
- A task can transition from incomplete (completed=False) to complete (completed=True) via the toggle operation
- A task can transition from complete (completed=True) back to incomplete (completed=False) via the toggle operation

## Relationships
- No explicit relationships between Task entities
- All tasks are managed within a single TodoService instance

## Constraints
- Task titles must not be empty
- Task IDs must be unique and auto-increment from 1
- All operations must be validated to prevent invalid states
- In-memory storage only - data is lost when application exits