#!/usr/bin/env python3

import sys
import fileinput
from pathlib import Path

text_to_search = "export VIRTUAL_ENV"
replacement_text = "\n".join([
    "",
    "if [ \"z\" != \"z$MSYSTEM\" ]; then",
    "\tVIRTUAL_ENV=`cygpath -u $VIRTUAL_ENV`",
    "fi",
    "",
    "export VIRTUAL_ENV"
])

venv_paths = [
    Path.home() / ".virtualenvs",
]

activate_suffixes = [
    "bin/activate",
    "Scripts/activate",
]

if len(sys.argv) != 2:
    print("Pass the path to the virtualenv to the script")
    exit(1)

venv_to_fix = sys.argv[1]

def find_path(venv_name):
    p = Path(venv_name)

    if p.exists():
        return p
    else:
        # Not an absolute path, search for it in the venv prefixes
        for prefix in venv_paths:
            maybe_p = Path(prefix) / p
            print(f"Looking for venv in {maybe_p}...")

            if maybe_p.exists():
                print("Found the venv!")
                return maybe_p

p = find_path(venv_to_fix)

if not p.exists():
    print(f"Virtualenv not found: {p}")
    exit(2)

if not p.is_dir():
    print("Pass the directory, not the file.")
    exit(3)

filename = None

def find_activate_file(p: Path):
    for suffix in activate_suffixes:
        filepath = p / suffix
        print(f"Looking for activate file in: {filepath}")

        if filepath.exists():
            print("Found the activate file!")
            return filepath

filename = find_activate_file(p)

if not filename:
    print("Couldn\'t find an activate file in the given directory")
    exit(4)

print(f"Updating file at {filename}...")

with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(text_to_search, replacement_text), end='')

print("Done!")
