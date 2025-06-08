import typer
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

app = typer.Typer()


@app.command()
def pipeline(
    framework: str = typer.Option(..., prompt="Choose a framework (laravel, django, react, flutter)"),
    target: str = typer.Option(..., prompt="Choose a deploy target (contabo, railway, render)")
):
    print(f"🛠  Generating pipeline for {framework} to deploy on {target}...")

    env = Environment(loader=FileSystemLoader(str(Path(__file__).parent.parent / "templates")))
    template = env.get_template("base_pipeline.yml.j2")

    output = template.render(framework=framework, target=target)

    output_dir = Path.cwd() / ".stackforge"
    output_dir.mkdir(exist_ok=True)
    (output_dir / "pipeline.yml").write_text(output)

    print("✅ Pipeline generated at `.stackforge/pipeline.yml`")
