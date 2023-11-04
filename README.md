# Bot Assistant

Bot Assistant is a command-line application that helps you manage your contacts and notes.

---

## Pre-requisites

* Python 3.8 or higher

## Installation

From the root directory of the project, run the following command:

```bash
pip install .
```

---

## Usage

To run the bot, simply type the following command in your terminal:

```bash
bot-assistant
```

To get a list of available commands, run `bot-assistant` and type `help`.

Please follow a guide below to learn more about the bot.

---

# Bot Assistant User Guide

Welcome to the Bot Assistant, your digital helper for managing contacts and taking notes efficiently.

Our bot comes with a suite of commands that allow you to add, modify, delete, and query your contact and notes information with ease.

## Features

- Contact Management: Add, edit, and delete contacts, along with their phone numbers, addresses, emails, and birthdays.
- Note-taking: Create and manage your notes with tags and statuses to keep your thoughts and tasks organized.
- Search Functionality: Quickly find contacts and notes with powerful search commands.
- Reminders: Get notified about upcoming birthdays.

## Getting Started

To get started, simply run the `bot-assistant` program in your terminal after installation.


## Contact Commands

Below is a table of commands related to contact management:

| Command       | Description                       | Example Usage                                           |
|---------------|-----------------------------------|---------------------------------------------------------|
| `hello`       | Say hello to the bot.             | `hello`                                                 |
| `add`         | Add a new contact.                | `add AlanWake 0987654321`                               |
| `edit`        | Edit a contact's name.            | `edit AlanWake AlanAwaken`                              |
| `add-phone`   | Add a phone to contact's list.    | `add-phone AlanWake 0987654322`                         |
| `delete`      | Delete a contact.                 | `delete AlanWake`                                       |
| `show-phone`  | Show a contact's phone.           | `phone AlanWake`                                        |
| `edit-phone`  | Edit a contact's phone number.    | `edit-phone AlanWake 0987654321 0987654322`             |
| `remove-phone`| Remove a contact's phone.         | `remove-phone AlanWake 0987654321`                      |
| `add-address` | Add a contact's address.          | `add-address AlanWake 6A Bright Falls Ave`              |
| `edit-address`| Change a contact's address.       | `edit-address AlanWake 6A Bright Falls Ave; 7A Bright Falls Ave` |
| `show-address`| Show a contact's address.         | `show-address AlanWake`                                 |
| `remove-address`| Remove a contact's address.     | `remove-address AlanWake 6A Bright Falls Ave`           |
| `add-email`   | Add an email to a contact.        | `add-email AlanWake alanwake@remedy.com`                |
| `show-email`  | Shows an email of a contact.      | `show-email AlanWake`                                   |
| `edit-email`  | Edit an email of a contact.       | `edit-email AlanWake alanwake@email.com alanwake1@remedy.com` |
| `remove-email`| Remove a contact's email.         | `remove-email AlanWake alanwake@remedy.com`             |
| `all`         | Show all contacts.                | `all`                                                   |
| `add-birthday`| Add a birthday to a contact.      | `add-birthday AlanWake 30.10.1982`                      |
| `show-birthday`| Show a contact's birthday.       | `show-birthday AlanWake`                                |
| `remove-birthday`| Remove a contact's birthday.   | `remove-birthday AlanWake`                              |
| `birthdays`   | Show all birthdays for a period.  | `birthdays 30`                                          |
| `find`        | Find contact records.             | `find 050`                                              |

## Notes Commands

For managing your notes, here's what you can do:

| Command             | Description                           | Example Usage                                   |
|---------------------|---------------------------------------|-------------------------------------------------|
| `add-note`          | Add a new note.                       | `add-note Investigation`                        |
| `add-tag`           | Add a tag to note by id.              | `add-tag 1 research`                            |
| `add-text`          | Add text to note by id.               | `add-text 1 We start research on Monday.`       |
| `override-text`     | Overrides note's text by id.          | `override-text 1 Research moved to Tuesday.`    |
| `change-note-status`| Change note's status by id.           | `change-note-status 1 in_progress`              |
| `remove-note`       | Remove a note by id.                  | `remove-note 1`                                 |
| `edit-note-title`   | Change note's title by id.            | `edit-note-title 1 detective_work`              |
| `remove-tag`        | Remove a tag of the note by id.       | `remove-tag 12 sunny`                           |
| `notes`             | Shows all notes.                      | `notes`                                         |
| `show-note`         | Shows specific notes by note id.              | `show-note 1`                               |
| `find-note`         | Shows all notes which contain the entered characters. | `find-note sun`                     |
| `find-notes-by-tag` | Shows notes by specified tag.                 | `find-notes-by-tag research`                |
| `help`              | Show this help message.                       | `help`                                      |


## Exit Commands

When you are done with your tasks, you can close the Bot Assistant using any of these commands:

- `close`
- `exit`
- `quit`
- `bye`

## Remove the bot from your machine

We hope that you enjoy using our bot!

If you wish to remove it from your machine, simply run the following command:

```bash
pip uninstall bot-assistant
```

---
## Contributing

If you want to contribute to the project, please follow the instructions below.

### Setup

Create a virtual environment:

```bash
python -m venv bot-assistant
```

Activate the virtual environment:

```bash
Linux:
source bot-assistant/bin/activate

Windows:
bot-assistant\Scripts\activate.bat
```

You can use any other virtual environment managers, like [poetry](https://python-poetry.org) or [pipenv](https://pipenv.pypa.io/en/latest/). It's up to you.

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
git checkout -b feat/jim/feature-1 master
```

When starting work on a bugfix, branch off from the `master` branch.

```bash
git checkout -b fix/<your_name>/<bug_name> master
```
Example:
```bash
git checkout -b fix/jim/bug-1 master
```

When a feature is complete, it is merged back into `master` by creating a pull request after a code review.
