import typer
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel
from pathlib import Path
from contribu.core.models.profile import load_profile
import json

app = typer.Typer()
console = Console()

PROFILE_PATH = Path.home() / ".contribu_profile.json"


@app.command()
def me():
    try:
        profile = load_profile()
        profile_info = (
            f"[bold]Name:[/bold] {profile.name}\n"
            f"[bold]GitHub Username:[/bold] {profile.github_username}\n"
            f"[bold]Email:[/bold] {profile.email}\n"
            f"[bold]Interests:[/bold] {', '.join(profile.interests)}"
        )
        console.print(Panel.fit(profile_info, title="Profile Details", border_style="green"))
    except FileNotFoundError:
        console.print(":warning: No profile found. Please run [bold]contribu init[/bold] to create a profile.")
    except json.JSONDecodeError:
        console.print(":warning: Profile file is corrupted. Please delete the file and run [bold]contribu init[/bold].")



