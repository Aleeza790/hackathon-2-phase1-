# Implementation Plan: CLI Todo CRUD Operations

**Branch**: `001-cli-todo-crud` | **Date**: 2025-12-31 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-cli-todo-crud/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a CLI-based todo application that allows users to manage tasks through an interactive REPL interface. The application will provide exactly 5 core features: adding tasks with title and optional description, listing all tasks with status indicators, updating task details by ID, deleting tasks by ID, and toggling task completion status. The application will store all data in-memory only, with no persistence after program exit, following the clean architecture pattern with separation of concerns across models, storage, and CLI layers.

## Technical Context

**Language/Version**: Python 3.13 (as specified in constitution)
**Primary Dependencies**: uv package manager, rich library (optional for formatting)
**Storage**: In-memory only (list or dict, no persistence after program exit)
**Testing**: Manual testing via console demo (no automated tests required for MVP)
**Target Platform**: Cross-platform command-line interface (Windows, macOS, Linux)
**Project Type**: Single CLI application
**Performance Goals**: Instant response for all operations (sub-second for any task manipulation)
**Constraints**:
  - Strictly in-memory storage (no file/DB persistence)
  - No additional features beyond 5 core operations (add, list, update, delete, toggle)
  - Follow exact 5-file structure: main.py, models.py, storage.py, cli.py, __init__.py
  - All functions must be <35 lines as per constitution
  - Type hints required on every function
  - Google-style docstrings required for all public functions
**Scale/Scope**: Single-user application, local usage only, no concurrent users

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Compliance Verification

**Project Structure Requirements (Principle I)**: ✅
- Implementation will follow exact 5-file structure: `src/main.py`, `src/models.py`, `src/storage.py`, `src/cli.py`, and `src/__init__.py`
- Architecture maintains clear separation: models (data structure), storage (business logic), cli (user interface)

**Data Model Constraints (Principle II)**: ✅
- Task model will contain: id (int, auto-increment from 1), title (str, required), description (str | None, optional), completed (bool, default False)
- Operations will be performed through the service class
- Internal data structures will not be exposed directly

**CLI Interface Requirements (Principle III)**: ✅
- Application will implement interactive REPL loop
- Will support commands: `add`, `list`/`ls`, `update`, `delete`/`del`, `done`/`toggle`, `help`/`?`
- Will provide clear, formatted output with visual indicators for completed tasks
- Will provide proper error messaging

**Code Quality Standards (Principle IV)**: ✅
- All code will follow PEP 8 + Python 3.13 style
- Type hints will be included on every function
- Google-style docstrings will be used
- Functions will be kept under 35 lines
- Descriptive names will be used
- Global variables will be avoided
- All error cases will be handled with clear user messages

**In-Memory Storage Implementation (Principle V)**: ✅
- All data will be stored in-memory only with no persistence after program exit
- InMemoryTodoService will handle all CRUD operations safely
- Invalid ID access will be prevented with proper error handling
- Data integrity will be maintained throughout all operations

**Dependency Management (Principle VI)**: ✅
- Only `rich` library will be used if needed for formatting
- Application will use Python 3.13 with `uv` as package manager

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```text
# [REMOVE IF UNUSED] Option 1: Single project (DEFAULT) - CLI Application
src/
├── __init__.py
├── main.py              # Program entry point + main loop
├── models.py            # Task data model
├── storage.py           # InMemoryTodoService (all CRUD logic)
└── cli.py               # Command parsing + user interface

tests/
├── contract/
├── integration/
└── unit/
```

**Structure Decision**: Following the constitution's exact 5-file structure requirement for CLI applications: main.py (entry point), models.py (data structure), storage.py (business logic), cli.py (user interface), and __init__.py.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No constitution violations identified. All implementation decisions align with the project constitution.
