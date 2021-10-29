# Example CLI with --version

Typer is great, but I was confused how to implement a `--version` command correctly. This works but is not terribly intuitive.

## Poetry config

In order to ensure `settings.json` works on your machine, make sure the following poetry setting is set before running `poetry install`:

```
poetry config virtualenvs.in-project true
```