"""In-memory storage service for the CLI Todo application."""
from typing import List, Optional
from .models import Task


class InMemoryTodoService:
    """
    Provides CRUD operations for tasks using in-memory storage.
    
    All data is stored in-memory only with no persistence after program exit.
    The service handles all CRUD operations safely and prevents invalid ID access
    with proper error handling. Data integrity is maintained throughout all operations.
    """
    
    def __init__(self) -> None:
        """Initialize the service with an empty task list and ID counter."""
        self._tasks: List[Task] = []
        self._next_id: int = 1
    
    def add_task(self, title: str, description: Optional[str] = None) -> int:
        """
        Add a new task with the given title and optional description.
        
        Args:
            title: The required title of the task (cannot be empty)
            description: Optional description of the task
            
        Returns:
            The ID of the newly created task
            
        Raises:
            ValueError: If title is empty or None
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")
        
        task = Task(
            id=self._next_id,
            title=title.strip(),
            description=description.strip() if description else None,
            completed=False
        )
        
        self._tasks.append(task)
        task_id = self._next_id
        self._next_id += 1
        
        return task_id
    
    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the system.
        
        Returns:
            A list of all tasks, sorted by ID
        """
        return sorted(self._tasks, key=lambda t: t.id)
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a specific task by its ID.
        
        Args:
            task_id: The ID of the task to retrieve
            
        Returns:
            The task if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update the title and/or description of an existing task.
        
        Args:
            task_id: The ID of the task to update
            title: New title (optional, if provided will replace existing)
            description: New description (optional, if provided will replace existing)
            
        Returns:
            True if the task was found and updated, False otherwise
            
        Raises:
            ValueError: If title is provided but is empty
        """
        if title is not None and (not title or not title.strip()):
            raise ValueError("Task title cannot be empty")
        
        for task in self._tasks:
            if task.id == task_id:
                if title is not None:
                    task.title = title.strip()
                if description is not None:
                    task.description = description.strip() if description else description
                return True
        return False
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.
        
        Args:
            task_id: The ID of the task to delete
            
        Returns:
            True if the task was found and deleted, False otherwise
        """
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                del self._tasks[i]
                return True
        return False
    
    def toggle_task_status(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task.
        
        Args:
            task_id: The ID of the task to toggle
            
        Returns:
            True if the task was found and status was toggled, False otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                task.completed = not task.completed
                return True
        return False
    
    def get_next_id(self) -> int:
        """
        Get the next available task ID.
        
        Returns:
            The next ID that will be assigned to a new task
        """
        return self._next_id