import typer
from pathlib import Path

app = typer.Typer()

@app.command()
def templates():
    templates_path = Path(__file__).parent.parent / "templates"
    if not templates_path.exists():
        print("\n❌ No templates directory found.")
        raise typer.Exit()

    templates = list(templates_path.glob("*.yml.j2"))
    if not templates:
        print("\n📭 No templates available.")
        return

    print("\n📦 Available StackForge Templates:\n")
    for tmpl in templates:
        name = tmpl.stem.replace("-", " ").replace(".yml", "")
        print(f"• {name}")
