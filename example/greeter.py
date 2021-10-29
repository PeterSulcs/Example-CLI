from typing import Optional
from example import __version__
import typer

app = typer.Typer()

@app.command("hello", help="say hello")
def hello(name: Optional[str] = typer.Argument(None)) -> None:
    typer.echo(f"Hello, {name}, version {__version__}!")

@app.command("bye", help="say goodbye")
def bye(name: Optional[str] = typer.Argument(None)) -> None:
    typer.echo(f"Good bye, {name}!")

def main():
    app()