# orca-uv-playground

Just playing around with uv (python packager) to learn before integrating it into Orca

## Installation

You need `uv`. Just `brew install uv` or one of the other options in the
https://docs.astral.sh/uv/getting-started/installation/ page.

## Projects

TODO.

## Scripts

See the `script-based` directory.

No deps, no problem:

```bash
uv run script-based/script-that-doesnt-need-it.py
```

Here's a script with a dependency, before we add the deps using uv:

```bash
❯ uv run script-based/script-that-needs-gitpython.py
Traceback (most recent call last):
  File "/Users/shay/src/orca-uv-playground/script-based/script-that-needs-gitpython.py", line 1, in <module>
    import git
ModuleNotFoundError: No module named 'git'
```

Here's how to add the dep:

```bash
❯ uv add --script script-based/script-that-needs-gitpython.py GitPython==3.1.42
Updated `script-based/script-that-needs-gitpython.py`
```

This will add the following to the file:

```py
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "gitpython==3.1.42",
# ]
# ///
```

And then when we run it:

```bash
❯ uv run script-based/script-that-needs-gitpython.py
Reading inline script metadata from: script-based/script-that-needs-gitpython.py
Installed 3 packages in 4ms
Current branch: main
```
