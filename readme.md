# Example project

This project is a cookie cutter for a basic Python project using:
- `lightning` for defining and trainig models.
- `pytest` for testing.
- `isort, `black` and `ruff` for formatting and linting.

It also includes a GitHub action which runs `pytest` on every push and pull-request.

## Set-up

```bash
pip install -r requirements.txt
pip install -e .
```

## Testing that you're good to go

```bash
python
> import example_package
> print(example_package.__version__)
```

## If you are developing this package...

Start by installing the developer dependencies

```bash
pip install -r requirements-dev.txt
```

### Installing pre-commit hooks

```bash
pip install pre-commit
pre-commit install
```

### Running tests

```bash
pip install -r requirements-dev.txt
pytest
```
