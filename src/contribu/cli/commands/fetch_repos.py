import typer
from rich.console import Console
from contribu.core.models.profile import load_profile
from contribu.core.repo_scanner import fetch_repos

app = typer.Typer()
console = Console()

@app.command()
def find_repos():
    print("🔍 Finding open source repos based on your profile...\n")
    try:
        profile = load_profile()
    except FileNotFoundError:
        console.print(":warning: No profile found. Please run [bold]contribu init[/bold] to create a profile.")
        raise typer.Exit(code=1)
    
    try:
        repos = fetch_repos(profile)
    except Exception as e:
        console.print(f":x: Error fetching repositories: {e}")
        raise typer.Exit(code=1)

    for i, repo in enumerate(repos, 1):
        print(f"{i}. {repo['name']} ⭐️ {repo['stars']}")
        print(f"   {repo['description']}")
        print(f"   {repo['url']}\n")
