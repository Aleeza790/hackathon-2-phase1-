"""Command-line interface for the CLI Todo application."""
import sys
from typing import List, Optional

try:
    from rich.console import Console
    from rich.table import Table
    from rich.text import Text
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

from .storage import InMemoryTodoService
from .models import Task


class TodoCLI:
    """
    Command-line interface for interacting with the todo application.
    
    Provides an interactive REPL loop supporting commands:
    - add: Add a new task
    - list/ls: List all tasks
    - update: Update a task by ID
    - delete/del: Delete a task by ID
    - done/toggle: Toggle task completion status
    - help/?: Show available commands
    - exit: Exit the application
    """
    
    def __init__(self, service: InMemoryTodoService) -> None:
        """
        Initialize the CLI with a todo service.

        Args:
            service: The InMemoryTodoService to interact with
        """
        self.service = service
        self.running = True
        if RICH_AVAILABLE:
            self.console = Console()
    
    def run(self) -> None:
        """Start the interactive REPL loop."""
        if RICH_AVAILABLE:
            self.console.print("[bold blue]Welcome to the Todo App![/bold blue]")
            self.console.print("Type 'help' for available commands or 'exit' to quit.")
        else:
            print("Welcome to the Todo App!")
            print("Type 'help' for available commands or 'exit' to quit.")

        while self.running:
            try:
                command_input = input("\n> ").strip()
                if not command_input:
                    continue

                self._process_command(command_input)
            except KeyboardInterrupt:
                if RICH_AVAILABLE:
                    self.console.print("\n[bold red]Exiting...[/bold red]")
                else:
                    print("\nExiting...")
                break
            except EOFError:
                if RICH_AVAILABLE:
                    self.console.print("\n[bold red]Exiting...[/bold red]")
                else:
                    print("\nExiting...")
                break
    
    def _process_command(self, command_input: str) -> None:
        """
        Parse and execute a command from user input.

        Args:
            command_input: The raw command string from user input
        """
        try:
            parts = command_input.split(maxsplit=1)
            command = parts[0].lower()
            args = parts[1] if len(parts) > 1 else ""

            if command in ['add']:
                self._handle_add(args)
            elif command in ['list', 'ls']:
                self._handle_list()
            elif command in ['update']:
                self._handle_update(args)
            elif command in ['delete', 'del']:
                self._handle_delete(args)
            elif command in ['done', 'toggle']:
                self._handle_toggle(args)
            elif command in ['help', '?']:
                self._handle_help()
            elif command in ['exit', 'quit']:
                self._handle_exit()
            else:
                print(f"Unknown command: {command}. Type 'help' for available commands.")
        except Exception as e:
            print(f"Error processing command: {e}. Type 'help' for available commands.")
    
    def _handle_add(self, args: str) -> None:
        """Handle the 'add' command to create a new task."""
        # Parse title and description from arguments
        title, description = self._parse_title_description(args)

        if not title:
            if RICH_AVAILABLE:
                self.console.print("[bold red]Error:[/bold red] Title is required. Usage: add \"title\" \"description\" (description is optional)")
            else:
                print("Error: Title is required. Usage: add \"title\" \"description\" (description is optional)")
            return

        try:
            task_id = self.service.add_task(title, description)
            if RICH_AVAILABLE:
                self.console.print(f"[bold green]Task added with ID: {task_id}[/bold green]")
            else:
                print(f"Task added with ID: {task_id}")
        except ValueError as e:
            if RICH_AVAILABLE:
                self.console.print(f"[bold red]Error: {e}[/bold red]")
            else:
                print(f"Error: {e}")
    
    def _handle_list(self) -> None:
        """Handle the 'list' command to display all tasks."""
        tasks = self.service.get_all_tasks()

        if not tasks:
            if RICH_AVAILABLE:
                self.console.print("[bold]No tasks yet[/bold]")
            else:
                print("No tasks yet")
            return

        if RICH_AVAILABLE:
            table = Table(title="Your Tasks", show_header=True, header_style="bold magenta")
            table.add_column("ID", style="dim", width=5)
            table.add_column("Status", width=10)
            table.add_column("Title", width=30)
            table.add_column("Description", width=50)

            for task in tasks:
                status = "✅" if task.completed else "❌"
                table.add_row(
                    str(task.id),
                    status,
                    task.title,
                    task.description if task.description else ""
                )

            self.console.print(table)
        else:
            print("\nYour tasks:")
            for task in tasks:
                status = "✅" if task.completed else "❌"
                print(f"{task.id}. [{status}] {task.title}")
                if task.description:
                    print(f"    {task.description}")
    
    def _handle_update(self, args: str) -> None:
        """Handle the 'update' command to modify a task."""
        parts = args.split(maxsplit=2)

        if len(parts) < 2:
            if RICH_AVAILABLE:
                self.console.print("[bold red]Error:[/bold red] Usage: update ID \"title\" \"description\" (title and description are optional but at least one must be provided)")
            else:
                print("Error: Usage: update ID \"title\" \"description\" (title and description are optional but at least one must be provided)")
            return

        try:
            task_id = int(parts[0])
        except ValueError:
            if RICH_AVAILABLE:
                self.console.print("[bold red]Error:[/bold red] Task ID must be a number")
            else:
                print("Error: Task ID must be a number")
            return

        # Parse the remaining parts for title and description
        remaining = ' '.join(parts[1:])
        title, description = self._parse_title_description(remaining)

        if title is None and description is None:
            if RICH_AVAILABLE:
                self.console.print("[bold red]Error:[/bold red] You must provide at least a title or description to update")
            else:
                print("Error: You must provide at least a title or description to update")
            return

        updated = self.service.update_task(task_id, title, description)
        if updated:
            if RICH_AVAILABLE:
                self.console.print(f"[bold green]Task {task_id} updated successfully[/bold green]")
            else:
                print(f"Task {task_id} updated successfully")
        else:
            if RICH_AVAILABLE:
                self.console.print(f"[bold red]Error: Task with ID {task_id} not found[/bold red]")
            else:
                print(f"Error: Task with ID {task_id} not found")
    
    def _handle_delete(self, args: str) -> None:
        """Handle the 'delete' command to remove a task."""
        if not args:
            if RICH_AVAILABLE:
                self.console.print("[bold red]Error:[/bold red] Usage: delete ID")
            else:
                print("Error: Usage: delete ID")
            return

        try:
            task_id = int(args.strip())
        except ValueError:
            if RICH_AVAILABLE:
                self.console.print("[bold red]Error:[/bold red] Task ID must be a number")
            else:
                print("Error: Task ID must be a number")
            return

        deleted = self.service.delete_task(task_id)
        if deleted:
            if RICH_AVAILABLE:
                self.console.print(f"[bold green]Task {task_id} deleted successfully[/bold green]")
            else:
                print(f"Task {task_id} deleted successfully")
        else:
            if RICH_AVAILABLE:
                self.console.print(f"[bold red]Error: Task with ID {task_id} not found[/bold red]")
            else:
                print(f"Error: Task with ID {task_id} not found")
    
    def _handle_toggle(self, args: str) -> None:
        """Handle the 'toggle' or 'done' command to change task completion status."""
        if not args:
            if RICH_AVAILABLE:
                self.console.print("[bold red]Error:[/bold red] Usage: toggle ID")
            else:
                print("Error: Usage: toggle ID")
            return

        try:
            task_id = int(args.strip())
        except ValueError:
            if RICH_AVAILABLE:
                self.console.print("[bold red]Error:[/bold red] Task ID must be a number")
            else:
                print("Error: Task ID must be a number")
            return

        toggled = self.service.toggle_task_status(task_id)
        if toggled:
            task = self.service.get_task_by_id(task_id)
            if task:
                status = "completed" if task.completed else "not completed"
                if RICH_AVAILABLE:
                    self.console.print(f"[bold green]Task {task_id} marked as {status}[/bold green]")
                else:
                    print(f"Task {task_id} marked as {status}")
        else:
            if RICH_AVAILABLE:
                self.console.print(f"[bold red]Error: Task with ID {task_id} not found[/bold red]")
            else:
                print(f"Error: Task with ID {task_id} not found")
    
    def _handle_help(self) -> None:
        """Handle the 'help' command to show available commands."""
        if RICH_AVAILABLE:
            self.console.print("\n[bold]Available commands:[/bold]")
            self.console.print("  add \"title\" \"description\"     - Add a new task (description is optional)")
            self.console.print("  list / ls                     - Show all tasks")
            self.console.print("  update ID \"title\" \"desc\"      - Update task title and/or description")
            self.console.print("  delete ID / del ID            - Delete a task")
            self.console.print("  done ID / toggle ID           - Mark task as done/undone")
            self.console.print("  help / ?                      - Show this help message")
            self.console.print("  exit                          - Exit the application")
        else:
            print("\nAvailable commands:")
            print("  add \"title\" \"description\"     - Add a new task (description is optional)")
            print("  list / ls                     - Show all tasks")
            print("  update ID \"title\" \"desc\"      - Update task title and/or description")
            print("  delete ID / del ID            - Delete a task")
            print("  done ID / toggle ID           - Mark task as done/undone")
            print("  help / ?                      - Show this help message")
            print("  exit                          - Exit the application")
    
    def _handle_exit(self) -> None:
        """Handle the 'exit' command to quit the application."""
        self.running = False
        if RICH_AVAILABLE:
            self.console.print("[bold blue]Goodbye![/bold blue]")
        else:
            print("Goodbye!")
    
    def _parse_title_description(self, args: str) -> tuple[Optional[str], Optional[str]]:
        """
        Parse title and description from command arguments.
        
        Args:
            args: The arguments string to parse
            
        Returns:
            A tuple of (title, description) where either can be None
        """
        if not args.strip():
            return None, None
        
        # Handle quoted arguments
        parts = []
        current_part = ""
        in_quotes = False
        i = 0
        
        while i < len(args):
            char = args[i]
            
            if char == '"':
                in_quotes = not in_quotes
            elif char == ' ' and not in_quotes:
                if current_part:
                    parts.append(current_part)
                    current_part = ""
            else:
                current_part += char
            
            i += 1
        
        # Add the last part if it exists
        if current_part:
            parts.append(current_part)
        
        title = parts[0] if len(parts) > 0 else None
        description = parts[1] if len(parts) > 1 else None
        
        return title, description