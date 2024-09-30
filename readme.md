# Example project

This project is a cookie cutter for a basic Python project using:
- `lightning` for defining and trainig models.
- `wandb` for logging.
- `pytest` for testing.
- `isort`, `black` and `ruff` for formatting and linting.

It also includes a GitHub action which runs `pytest` on every push and pull-request.

## Set-up

```bash
pip install -r requirements.txt
pip install -e .
```

## Testing that you're good to go

```python
# in Python
import example_package

print(example_package.__version__)
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

## More resources

### More on `git` and using the terminal

- The Carpentries has amazing courses for [using the terminal/shell scripting](https://swcarpentry.github.io/shell-novice/) and for [`git`](https://swcarpentry.github.io/git-novice/). Take a look if you need a refresher.

### Structuring ML projects

- [Nicki's notes are amazing.](https://skaftenicki.github.io/dtu_mlops/)

### Setting up your editor and terminal for success

- I would recommend looking into having `black` run automatically on file save. For VSCode users, [follow these instructions](https://code.visualstudio.com/docs/python/formatting).
- I would also recommend having your editor highlight linting problems with your files. For VSCode users, [follow these instructions](https://code.visualstudio.com/docs/python/linting).
- If you are using mac, I suggest installing the following
    - [iTerm2](https://iterm2.com/), a prettier terminal replacement.
    - [`zsh` and `oh-my-zsh`](https://ohmyz.sh/), a replacement for `bash` that is prettier and better with auto-completes.

