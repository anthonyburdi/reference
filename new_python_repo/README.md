# New Python Repo

NOTE: This is a work in progress.

## About

This folder is meant to contain default settings to include in any new python repository. Command examples are for macOS.

## Steps

### Github

I find it easier to create a repo + first commit from the github UI, then clone locally (vs git init and push).

Click the new repo button and add a readme, gitignore and license. Set the name and public/private.

Once the repo is created, clone locally and modify the stubs you created via the UI (e.g. Readme, gitignore).

### Local

See also: setup.sh

These steps assume you want to use the latest patch version of python 3.11. E.g. `3.11.10`. Replace with your preferred python version.

### Global Setup

These are prerequisites to install before creating all repos.

1. `brew install pyenv` - Install pyenv to manage python versions
1. `pyenv init` - Follow instructions to load pyenv automatically
1. `pyenv install 3.11` - Make sure python version you want to use is installed via pyenv
1. `pyenv global 3.11` - Set the global python version (optional but recommended)
1. `brew install pipx` - Install pipx
1. `pipx ensurepath` - Set up pipx
1. `pipx install poetry` - Use pipx to install poetry

### Repo Setup

1. `pyenv local 3.11` - Set pyenv version
1. `poetry init` - Set up Poetry for this repo
1. `poetry shell` - If you haven't installed the python version you want to use, see Global Setup. Then change the poetry env using `poetry env use 3.11` (for python v3.11.latest)
1. `poetry add --group dev 'ruff'` - For linting
1. `poetry add --group dev 'mypy'` - For type checking
1. `poetry add --group dev 'pre-commit'` - For running linting on commit. See example config in this directory.
1. `poetry lock` - Commit the output of locking. Update this when changing dependencies. This will allow for repeatable builds.
1. `poetry install` - Install the dependencies you specified

## Tools & Settings

- [pyenv](https://github.com/pyenv/pyenv)
- [pipx](https://pipx.pypa.io/stable/installation/)
- [poetry](https://python-poetry.org/docs/)
- [ruff](https://docs.astral.sh/ruff/)
