import typer
from cli.commands import init, list


app = typer.Typer()

# Mount the `init` command group from cli/commands/init.py
app.add_typer(init.app, name="init")
app.add_typer(list.app, name="list")

if __name__ == "__main__":
    app()
