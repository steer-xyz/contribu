import typer
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel
from pathlib import Path
from contribu.core.models.profile import UserProfile, save_profile
import json

app = typer.Typer()
console = Console()

PROFILE_PATH = Path.home() / ".contribu_profile.json"


@app.command()
def init():
    console.print(Panel.fit("👋 Welcome to [bold magenta]Contribu CLI[/bold magenta]!\nLet's set up your profile."))

    name = Prompt.ask("👤 What is your [bold]name[/bold]?")
    github_username = Prompt.ask("🐙 What is your [bold]GitHub username[/bold]?")
    email = Prompt.ask("📫 What is your [bold]email[/bold]?")
    interests = Prompt.ask("🤖 What are your [bold]ML/AI interests[/bold]? (comma separated)")

    console.print(Panel.fit(f"Here’s what you entered:\n[bold]Name:[/bold] {name}\n[bold]GitHub:[/bold] {github_username}\n[bold]Email:[/bold] {email}\n[bold]Interests:[/bold] {interests}"))
    
    confirm = Prompt.ask("✅ Save this profile?", choices=["yes", "no"], default="yes")

    if confirm == "yes":
        profile = UserProfile(
            name=name,
            github_username=github_username,
            email=email,
            interests=[i.strip() for i in interests.split(",")]
        )
        save_profile(profile)
        console.print(f":white_check_mark: Profile saved to [bold green]{PROFILE_PATH}[/bold green]")
    else:
        console.print("❌ Profile not saved.")
