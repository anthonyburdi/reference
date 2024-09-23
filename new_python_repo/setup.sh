#!/bin/bash

source logging.sh

print_orange_header "Installing pyenv & python 3.11"
brew install pyenv
pyenv install 3.11

print_orange_header "Installing pipx"
brew install pipx
pipx ensurepath

print_orange_header "Installing poetry"
pipx install poetry

print_orange_header "You are set up globally. Now follow the Repo Specific instructions."
