import typer
from contribu.cli.commands import fetch_repos, init, me

app = typer.Typer()

app.command()(init.init)
app.command()(me.me)
app.command()(fetch_repos.find_repos)

if __name__ == "__main__":
    app()
