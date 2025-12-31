"""Main entry point for the CLI Todo application."""
from .storage import InMemoryTodoService
from .cli import TodoCLI


def main() -> None:
    """Main entry point for the application."""
    # Initialize the service and CLI
    service = InMemoryTodoService()
    cli = TodoCLI(service)
    
    # Run the application
    cli.run()


if __name__ == "__main__":
    main()