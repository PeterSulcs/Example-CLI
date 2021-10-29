from typing import Optional

import typer

from example import __version__

app = typer.Typer()


def version_callback(value: bool):
    if value:
        typer.echo(f"Greeter CLI Version: {__version__}")
        raise typer.Exit()


@app.command("hello", help="say hello")
def hello(name: Optional[str] = typer.Argument(None)) -> None:
    typer.echo(f"Hello, {name}!")


@app.command("bye", help="say goodbye")
def bye(name: Optional[str] = typer.Argument(None)) -> None:
    typer.echo(f"Good bye, {name}!")


@app.callback(invoke_without_command=True, no_args_is_help=True)
def base(
    version: Optional[bool] = typer.Option(
        None, "--version", callback=version_callback, is_eager=True
    )
):
    pass


def main():
    app()
