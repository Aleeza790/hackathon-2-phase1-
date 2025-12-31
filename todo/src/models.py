"""Task data model for the CLI Todo application."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a task in the todo application.
    
    Attributes:
        id: Unique identifier for the task, auto-incremented starting from 1
        title: Required title of the task, cannot be empty
        description: Optional description of the task, defaults to None
        completed: Boolean indicating whether the task is completed, defaults to False
    """
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False