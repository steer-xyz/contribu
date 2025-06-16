import typer
from contribu.cli.commands import fetch_repos, init, suggest_prs, me

app = typer.Typer()

app.command()(init.init)
app.command()(me.me)
app.command()(fetch_repos.fetch_repos)
# app.command()(suggest_prs.run)

if __name__ == "__main__":
    app()
