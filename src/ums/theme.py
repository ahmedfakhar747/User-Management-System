from rich.console import Console

console = Console()

def print_header(title: str, emoji: str) -> None:
    """Print a premium-style header for CLI sections."""
    text = f"[red]━━━[/red][yellow]━━━[/yellow][green] {emoji} {title.strip().upper()} {emoji}  [green]━━━[/green][cyan]━━━[/cyan]"
    console.rule(f"[bold cyan]{text}[/bold cyan]", align="center")


def print_success(message: str) -> None:
    """Print a success message."""
    console.print(f"✔️ [bold green]{message}[/bold green]")


def print_error(message: str) -> None:
    """Print an error message."""
    console.print(f"❌ [bold red]{message}[/bold red]")


def print_info(message: str) -> None:
    """Print an informational message."""
    console.print(f"ℹ️ [bold blue]{message}[/bold blue]")
