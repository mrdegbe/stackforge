import typer
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

app = typer.Typer()

TEMPLATE_DIR = Path(__file__).parent.parent / "templates"
OUTPUT_DIR = Path(".stackforge")
OUTPUT_DIR.mkdir(exist_ok=True)

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))


@app.command()
def pipeline(
    template: str = typer.Option(None, help="Name of template (e.g. laravel-railway)"),
    framework: str = typer.Option(
        None, help="Project framework (e.g. laravel, django)"
    ),
    target: str = typer.Option(None, help="Deploy target (e.g. railway, render)"),
):
    if template and (framework or target):
        typer.echo(
            "❌ Please use either --template OR (--framework and --target), not both."
        )
        raise typer.Exit(code=1)

    # Derive template name
    if template:
        template_name = f"{template}.yml.j2"
    elif framework and target:
        template_name = f"{framework.lower()}-{target.lower()}.yml.j2"
    else:
        typer.echo(
            "❌  Missing required options. Use --template OR --framework and --target."
        )
        raise typer.Exit(code=1)

    template_path = TEMPLATE_DIR / template_name
    if not template_path.exists():
        typer.echo(f"❌  Template not found: {template_name}")
        raise typer.Exit(code=1)

    typer.echo(f"🛠  Generating pipeline from template: {template_name}...")

    template_obj = env.get_template(template_name)
    output = template_obj.render()

    output_path = OUTPUT_DIR / "pipeline.yml"
    output_path.write_text(output, encoding="utf-8")

    typer.echo(f"✅ Pipeline generated at `{output_path}`")


# We were using this when --framework and --target were the only option (Don't get rid of this code)
# @app.command()
# def pipeline(
#     framework: str = typer.Option(..., prompt="Choose a framework (laravel, django, react, flutter)"),
#     target: str = typer.Option(..., prompt="Choose a deploy target (contabo, railway, render)")
# ):
#     print(f"🛠  Generating pipeline for {framework} to deploy on {target}...")
#
#     env = Environment(loader=FileSystemLoader(str(Path(__file__).parent.parent / "templates")))
#     template = env.get_template("base_pipeline.yml.j2")
#
#     output = template.render(framework=framework, target=target)
#
#     output_dir = Path.cwd() / ".stackforge"
#     output_dir.mkdir(exist_ok=True)
#     (output_dir / "pipeline.yml").write_text(output)
#
#     print("✅ Pipeline generated at `.stackforge/pipeline.yml`")
