## Master Computer Science DATA 1

### Bot Assistant

Python package to demonstrate simple bot assistant.

* basic functionality with common errors handling
* simple tests with assertions
* state file (serialized with pickle) is stored locally

---

## Installation

From the root directory of the project, run the following command:

```bash
pip install .
```

---

## Usage

### Bot Assistant

```bash
bot-assistant
```

To get a list of available commands, run `bot-assistant` and type `help`.

---

## Cleanup

```bash
pip uninstall bot-assistant
```

---

## Development

### Setup

Install the development requirements:

```bash
pip install -r dev-requirements.txt
```

### Style Guide

This project follows the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.

[black](https://pypi.org/project/black/#description) formatter is used to enforce the style guide.

To format the code, run the following command:

```bash
black .
```

For branches, we use the following naming convention:

```bash
<type>/<your_name>/<feature_name>
```

kebab-case is used for branch names.

[conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) are used for commit messages.

### Branching

We use `master` as the main branch where the source code of `HEAD` always reflects a production-ready state.

When starting work on a new feature, branch off from the `master` branch.

```bash
git checkout -b feat/<your_name>/<feature_name> master
```
Example:
```bash
git checkout -b feat/roman/feature-1 master
```

When starting work on a bugfix, branch off from the `master` branch.

```bash
git checkout -b fix/<your_name>/<bug_name> master
```
Example:
```bash
git checkout -b fix/roman/bug-1 master
```

When a feature is complete, it is merged back into `master` by creating a pull request after a code review.
