---

description: "Task list for CLI Todo Application implementation"
---

# Tasks: CLI Todo CRUD Operations

**Input**: Design documents from `/specs/001-cli-todo-crud/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md

**Tests**: No automated tests required per spec - manual testing via console demo

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure with exact 5 files: main.py, models.py, storage.py, cli.py, __init__.py
- [x] T002 Initialize Python 3.13 project with uv package manager
- [x] T003 [P] Configure linting and formatting tools following PEP 8 + Python 3.13 style
- [x] T004 [P] Set up type checking configuration for mandatory type hints

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 [P] Create Task data model in src/models.py with id, title, description, completed fields
- [x] T006 [P] Implement InMemoryTodoService in src/storage.py with CRUD operations
- [x] T007 Create base CLI interface structure in src/cli.py with command parsing
- [x] T008 Implement error handling and validation for all operations
- [x] T009 Setup main application loop in src/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Implement the ability to add new tasks with title and optional description

**Independent Test**: Can be fully tested by running the CLI app and executing the 'add' command with a title and optional description, then verifying the task appears in the list.

### Implementation for User Story 1

- [x] T010 [US1] Implement add_task method in InMemoryTodoService in src/storage.py
- [x] T011 [US1] Add command parsing for 'add' command in src/cli.py
- [x] T012 [US1] Implement UI feedback for successful task creation in src/cli.py
- [x] T013 [US1] Add validation to prevent empty titles in src/storage.py
- [x] T014 [US1] Test add functionality with title and description in manual testing

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View/List Tasks (Priority: P1)

**Goal**: Implement the ability to view all tasks with ID, status, title, and description

**Independent Test**: Can be fully tested by adding some tasks and then running the 'list' command to see all tasks with their status and details.

### Implementation for User Story 2

- [x] T015 [US2] Implement get_all_tasks method in InMemoryTodoService in src/storage.py
- [x] T016 [US2] Add command parsing for 'list'/'ls' commands in src/cli.py
- [x] T017 [US2] Implement formatted display of tasks with status indicators in src/cli.py
- [x] T018 [US2] Add "No tasks yet" message when list is empty in src/cli.py
- [x] T019 [US2] Test list functionality with various task states in manual testing

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Task Complete/Incomplete (Priority: P2)

**Goal**: Implement the ability to mark tasks as complete or incomplete by toggling their status

**Independent Test**: Can be fully tested by adding a task, then using the 'toggle' or 'done' command to change its completion status.

### Implementation for User Story 3

- [x] T020 [US3] Implement toggle_task_status method in InMemoryTodoService in src/storage.py
- [x] T021 [US3] Add command parsing for 'done'/'toggle' commands in src/cli.py
- [x] T022 [US3] Implement UI feedback for status change in src/cli.py
- [x] T023 [US3] Add error handling for invalid task IDs in src/storage.py
- [x] T024 [US3] Test toggle functionality in manual testing

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Update Task Details (Priority: P2)

**Goal**: Implement the ability to update the title and/or description of a task by ID

**Independent Test**: Can be fully tested by adding a task and then using the 'update' command to change its title and/or description.

### Implementation for User Story 4

- [x] T025 [US4] Implement update_task method in InMemoryTodoService in src/storage.py
- [x] T026 [US4] Add command parsing for 'update' command in src/cli.py
- [x] T027 [US4] Implement UI feedback for successful updates in src/cli.py
- [x] T028 [US4] Add validation to prevent empty titles in src/storage.py
- [x] T029 [US4] Test update functionality with various parameters in manual testing

---

## Phase 7: User Story 5 - Delete Task (Priority: P2)

**Goal**: Implement the ability to delete tasks by specifying their ID

**Independent Test**: Can be fully tested by adding tasks and then using the 'delete' command to remove a specific task.

### Implementation for User Story 5

- [x] T030 [US5] Implement delete_task method in InMemoryTodoService in src/storage.py
- [x] T031 [US5] Add command parsing for 'delete'/'del' commands in src/cli.py
- [x] T032 [US5] Implement UI feedback for successful deletion in src/cli.py
- [x] T033 [US5] Add error handling for invalid task IDs in src/storage.py
- [x] T034 [US5] Test delete functionality in manual testing

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T035 [P] Add comprehensive help command with usage instructions in src/cli.py
- [x] T036 [P] Implement error handling for invalid command syntax in src/cli.py
- [x] T037 [P] Add handling for special characters in titles and descriptions in src/storage.py
- [x] T038 [P] Improve output formatting using rich library if available in src/cli.py
- [x] T039 [P] Add proper exit command to gracefully close the application in src/main.py
- [x] T040 [P] Update README.md with complete setup instructions and command reference
- [x] T041 [P] Run comprehensive manual testing of all 5 features
- [x] T042 [P] Code cleanup and refactoring to ensure functions <35 lines

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Models before services
- Services before UI/cli components
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Implement add_task method in InMemoryTodoService in src/storage.py"
Task: "Add command parsing for 'add' command in src/cli.py"
Task: "Implement UI feedback for successful task creation in src/cli.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence