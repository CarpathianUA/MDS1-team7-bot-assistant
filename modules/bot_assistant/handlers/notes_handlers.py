#! ignore this line
# pylint: disable=redefined-builtin
# pylint: disable=redefined-outer-name

"""Module providing handlers for notes."""
from modules.bot_assistant.models.exceptions import (
    InvalidArgsError,
    InvalidIdValueError,
    InvalidSearchPatternError,
)
from modules.bot_assistant.decorators.decorators import input_error


@input_error
def add_note(args, notes):
    """Function adds a note."""

    if len(args) < 1:
        raise InvalidArgsError
    title = " ".join(args[0:])
    num = notes.add_note(title)
    return f"Note #'{num}' added."


@input_error
def add_tag(args, notes):
    """Function adds a tag."""

    if len(args) != 2:
        raise InvalidArgsError
    try:
        id = int(args[0])
    except ValueError as e:
        raise InvalidIdValueError from e

    tag = args[1]

    notes.add_tag(id, tag)
    return f"Note #'{id}': tag '{tag}' added."


def change_status(args, notes):
    """Function changes a status."""

    if len(args) != 2:
        raise InvalidArgsError
    try:
        id = int(args[0])
    except ValueError as e:
        raise InvalidIdValueError from e

    status = args

    notes.change_status(id, status)
    return f"Note #'{id}': status changed to '{status}'."


@input_error
def remove_note(args, notes):
    """Function removes a note."""

    if len(args) != 1:
        raise InvalidArgsError
    notes.remove_note(id)
    return f"Note #'{id}' deleted"


@input_error
def edit_title(args, notes):
    pass


@input_error
def add_text(args, notes):
    """Function adds a text."""

    if len(args) < 2:
        raise InvalidArgsError
    try:
        id = int(args[0])
    except ValueError as e:
        raise InvalidIdValueError from e

    text = " ".join(args[1:])

    notes.add_text(id, text)
    return f"Note #'{id}': text added."


@input_error
def remove_tag(args, notes):
    pass


@input_error
def notes(args, notes):
    """Function shows all notes."""

    return notes.get_all_notes()


@input_error
def find_note(args, notes):
    """Function finds notes by symbols."""

    if len(args) != 1:
        raise InvalidArgsError
    symbols = args[0]

    if len(symbols) < 2:
        raise InvalidSearchPatternError

    result = notes.find_note(symbols)
    if result:
        return result
    return "Nothing was found for the specified string."


@input_error
def find_note_by_filter(args, notes):
    pass
