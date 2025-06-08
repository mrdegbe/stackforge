import typer
from cli.commands import init


app = typer.Typer()

# Mount the `init` command group from cli/commands/init.py
app.add_typer(init.app, name="init")

if __name__ == "__main__":
    app()
