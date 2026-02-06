import os
import readchar
import re
from .models import User, UserDatabase
from ..theme import print_header, print_error, print_success, print_info
from rich.console import Console
from rich.table import Table

console = Console()


def clear_console():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    """Pause execution and wait for user input."""
    console.print("[dim]Press any key to continue…[/dim]")
    readchar.readkey()
    console.print()  # newline


def exit_program() -> None:
    """Exit the application gracefully."""
    print_header("GOODBYE", "👋")
    console.print(
        "\n[bold yellow]Thank you for using the User Management System![/bold yellow]"
    )
    console.rule()


def display_menu() -> None:
    """Display the main menu."""
    clear_console()
    print_header("User Management System", "⚙️")
    console.print(
        "[bold magenta]Welcome to the User Management System![/bold magenta]"
    )
    from rich import box
    table = Table(box=box.ROUNDED, show_header=True, header_style="bold cyan")
    commands = [
        ("1. ", "➕  Add User", "Add a new user to the system"),
        ("2. ", "🔍  Search User", "Search for a user by username"),
        ("3. ", "🗑️  Delete User", "Remove a user from the system"),
        ("4. ", "✏️  Update User", "Update user information"),
        ("5. ", "👁️  See All Users", "Display all registered users"),
        ("6. ", "⛔  Exit", "Exit the application"),
    ]
    table.add_column("#", justify="left", no_wrap=True, width=3)
    table.add_column("Command", justify="center", style="magenta", width=30)
    table.add_column("Description", style="green", width=50)
    for sr, command, description in commands:
        table.add_row(sr, f"[bold blue]{command}[/bold blue]", description)
    console.print(table)
    console.print("_" * 93)


def email_is_valid(email: str) -> bool:
    """Validate email format using regex."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def run():
    """Command-line interface for user management system."""
    db = UserDatabase()
    while True:
        clear_console()
        display_menu()
        option = input("Enter your option: ").strip().lower()

        match option:
            case "add user" | "1":
                clear_console()
                print_header("Adding User...", "➕")
                user = User(
                    input("Enter username: ").strip(),
                    input("Enter fullname: ").strip(),
                    input("Enter Email Address: ").strip(),
                )
                if not user.username:
                    print_error("Username cannot be empty")
                    pause()
                    continue
                if not user.name:
                    print_error("Name cannot be empty")
                    pause()
                    continue
                if not email_is_valid(user.email) or not user.email:
                    print_error("Missing or Invalid Email format.")
                    pause()
                    continue
                db.insert(user)
                pause()

            case "search user" | "2":
                clear_console()
                print_header("Searching User...", "🔍")
                username = input("Enter username: ").strip()
                user = db._find_user_by_username(username)
                if user:
                    print_success(f"User '{username}' Found!")
                    console.print(user, style="bold green")
                else:
                    print_error(f"User '{username}' not Found!")
                pause()

            case "delete user" | "3":
                clear_console()
                print_header("Deleting User...", "🗑️")
                username = input("Enter username: ").strip()
                db.delete(username)
                pause()

            case "update user" | "4":
                clear_console()
                print_header("Updating User...", "✏️")
                current_username = input("Enter current username to update: ").strip()
                new_username = (
                    input("Enter new username (leave blank to skip): ").strip() or None
                )
                new_name = (
                    input("Enter new fullname (leave blank to skip): ").strip() or None
                )
                new_email = (
                    input("Enter new Email Address (leave blank to skip): ").strip()
                    or None
                )

                if new_email is not None and not email_is_valid(new_email):
                    print_error("Invalid Email format.")
                    pause()
                    continue
                db.update(current_username, new_username, new_name, new_email)
                pause()

            case "see all users" | "5":
                clear_console()
                print_header("All Registered Users...", "📋")
                db.list_all()
                pause()

            case "exit" | "6":
                clear_console()
                if (
                    input("Are you sure you want to exit? (y/n): ").strip().lower()
                    == "y"
                ):
                    exit_program()
                    break

            case _:
                clear_console()
                print_error(f"Input '{option}' is unknown...")
                pause()
