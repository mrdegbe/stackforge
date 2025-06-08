import typer

app = typer.Typer()

@app.command()
def pipeline():
    print("🛠  Initializing a StackForge pipeline...")
