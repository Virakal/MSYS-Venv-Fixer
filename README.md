# MSYS Virtualenv Fixer

## Description

Out of the box, a virtualenv created on MSYS sets an incorrect `VIRTUAL_ENV` environment variable, using Windows-style paths instead of Unix.
This script updates the file to fix that.

## Usage

`fix_venv.py [path-to-virtualenv]`

## Convenience

By default, if you pass a name instead of a path the script will search in `~/.virtualenvs`. You can add to the search path by adding to the `venv_paths` array in the script, assuming you are comfortable enough with Python.
