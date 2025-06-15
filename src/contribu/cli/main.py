import typer
from contribu.cli.commands import init, find_repos, suggest_prs

app = typer.Typer()

app.command()(init.init)
app.command()(find_repos.run)
# app.command()(suggest_prs.run)

if __name__ == "__main__":
    app()
