# I have done inserting, saving, and loading function and delete, update functions are remaining to update

import json
from pathlib import Path

from rich.table import Table
from rich.console import Console

console = Console()


class User:
    def __init__(self, username: str, name: str, email: str):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return (
            f"User(username='{self.username}', "
            f"name='{self.name}', email='{self.email}')"
        )

    def __str__(self) -> str:
        return (
            f"Username: {self.username}\n" f"Name: {self.name}\n" f"Email: {self.email}"
        )


class UserDatabase:
    def __init__(self, filepath: str = "data/users.json"):
        """Initialize the user database with a JSON file path."""
        self.users: list[User] = []
        self.filepath = filepath
        self.load_users()


    def __repr__(self) -> str:
        if not self.users:
            return "<UserDatabase empty>"

        preview = ", ".join(u.username for u in self.users[:3])
        more = "" if len(self.users) <= 3 else f", +{len(self.users) - 3} more"
        return f"<UserDatabase users={len(self.users)} [{preview}{more}]>"

    # ---------- helpers ----------

    def load_users(self) -> None:
        """Load users from the JSON file."""
        if Path(self.filepath).exists():
            try:
                data = json.loads(Path(self.filepath).read_text())
                for user_data in data:
                    if not self._find_user_by_username(user_data['username']) and not self._find_user_by_email(user_data['email']):
                        try:
                            user = User(
                                user_data['username'],
                                user_data['name'],
                                user_data['email']
                            )
                            self.users.append(user)
                        except ValueError:
                            pass # Skip invalid entries
            except json.JSONDecodeError:
                self.users = []  # Start fresh if corrupted

    def save_users(self) -> None:
        """Save all users to JSON file."""
        data = [
            {
                "username": u.username,
                "name": u.name,
                "email": u.email,
            }
            for u in self.users
        ]

        # Create directory if it doesn't exists
        Path(self.filepath).parent.mkdir(parents=True, exist_ok=True)

        # Save to file
        Path(self.filepath).write_text(json.dumps(data, indent=4))

    def _find_user_by_username(self, username: str) -> User | None:
        """Search for a user by username."""
        username = username.lower()
        return next(
            (u for u in self.users if u.username.lower() == username),
            None,
        )

    def _find_user_by_email(self, email: str) -> User | None:
        """Search for a user by email."""
        email = email.lower()
        return next(
            (u for u in self.users if u.email.lower() == email),
            None,
        )

    def _insert_sorted(self, user: User) -> None:
        i = 0
        while i < len(self.users):
            if self.users[i].username.lower() > user.username.lower():
                break
            i += 1
        self.users.insert(i, user)

    # ---------- public API ----------

    def insert(self, user: User) -> bool:
        """Insert user and save to JSON."""
        if not isinstance(user, User):
            user_repr = getattr(user, "username", str(user))  # try to show username if possible
            console.print(
                f"[bold red]Error:[/bold red] '{user_repr}' is not a valid User object"
            )
            return False

        if self._find_user_by_username(user.username):
            console.print(
                f"[bold red]Error:[/bold red] Username "
                f"'[yellow]{user.username}[/yellow]' already exists"
            )
            return False

        if self._find_user_by_email(user.email):
            console.print(
                f"[bold red]Error:[/bold red] Email "
                f"'[yellow]{user.email}[/yellow]' already exists"
            )
            return False

        if len(user.username) > 10:
            console.print(
                f"[bold red]Error:[/bold red] Username "
                f"'[yellow]{user.username}[/yellow]' is too long"
            )
            return False

        import bisect
        bisect.insort(self.users, user, key=lambda u: u.username.lower())
        self.save_users() # <- Save after insert
        console.print(f"[green]✔ User '{user.username}' added successfully[/green]")
        return True

    def list_all(self) -> None:
        """Display all users in the database."""
        if not self.users:
            console.print("[yellow]No users in database[/yellow]")
            return

        table = Table(title="User Database")
        table.add_column("#", justify="right", style="cyan")
        table.add_column("Username", style="magenta", width=20)
        table.add_column("Name", style="green", width=25)
        table.add_column("Email", style="yellow", width=30)

        for i, user in enumerate(self.users, start=1):
            table.add_row(str(i), user.username, user.name, user.email)

        console.print(table)

    def delete(self, username: str) -> bool:
        """Delete a user from the database."""
        user = self._find_user_by_username(username)
        if not user:
            console.print(
                f"[bold red]Error:[/bold red] Username "
                f"'[yellow]{username}[/yellow]' not found"
            )
            return False

        self.users.remove(user)
        self.save_users()  # ← Save after delete
        console.print(f"[green]✔ User '{user.username}' deleted successfully[/green]")
        return True

    def update(
        self,
        username: str,
        new_username: str | None = None,
        new_name: str | None = None,
        new_email: str | None = None,
    ) -> bool:
        """Update user information."""
        user = self._find_user_by_username(username)
        if not user:
            console.print(
                f"[bold red]Error:[/bold red] Username "
                f"'[yellow]{username}[/yellow]' not found"
            )
            return False

        if new_username and new_username.lower() != user.username.lower():
            if self._find_user_by_username(new_username):
                console.print(
                    f"[bold red]Error:[/bold red] Username "
                    f"'[yellow]{new_username}[/yellow]' already exists"
                )
                return False

        if new_email and new_email.lower() != user.email.lower():
            if self._find_user_by_email(new_email):
                console.print(
                    f"[bold red]Error:[/bold red] Email "
                    f"'[yellow]{new_email}[/yellow]' already exists"
                )
                return False

        old_username = user.username

        if new_username:
            user.username = new_username
        if new_name:
            user.name = new_name
        if new_email:
            user.email = new_email

        if new_username:
            self.users.remove(user)
            self._insert_sorted(user)

        self.save_users() # ← Save after update
        console.print(f"[green]✔ User '{old_username}' updated successfully[/green]")
        return True
