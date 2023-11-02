from modules.bot_assistant.models.exceptions import (
    InvalidArgsError,
    InvalidIdValueError,
    InvalidSearchPatternError,
)
from modules.bot_assistant.decorators.decorators import input_error


@input_error
def add_note(args, notes_engine):
    if len(args) < 1:
        raise InvalidArgsError
    title = " ".join(args[0:])
    num = notes_engine.add_note(title)
    return f"Note #'{num}' added."


@input_error
def add_tag(args, noteslist):
    if len(args) != 2:
        raise InvalidArgsError
    try:
        note_id = int(args[0])
    except ValueError as e:
        raise InvalidIdValueError from e

    tag = args[1]

    noteslist.add_tag(note_id, tag)
    return f"Note #'{note_id}': tag '{tag}' added."


@input_error
def change_status(args, notes_engine):
    if len(args) != 2:
        raise InvalidArgsError
    try:
        note_id = int(args[0])
    except ValueError as e:
        raise InvalidIdValueError from e

    status = args[1]

    notes_engine.change_status(note_id, status)
    return f"Note #'{note_id}': status changed to '{status}'."


@input_error
def remove_note(args, notes_engine):
    if len(args) != 1:
        raise InvalidArgsError
    try:
        note_id = int(args[0])
    except ValueError as e:
        raise InvalidIdValueError from e

    notes_engine.remove_note(note_id)
    return f"Note #'{note_id}' deleted"


@input_error
def edit_title(args, notes_engine):
    if len(args) < 2:
        raise InvalidArgsError
    try:
        note_id = int(args[0])
    except ValueError as e:
        raise InvalidIdValueError from e

    title = " ".join(args[1:])

    notes_engine.edit_title(note_id, title)
    return f"Note #'{note_id}': title edited."


@input_error
def add_text(args, notes_engine):
    if len(args) < 2:
        raise InvalidArgsError
    try:
        note_id = int(args[0])
    except ValueError as e:
        raise InvalidIdValueError from e

    text = " ".join(args[1:])

    notes_engine.add_text(note_id, text)
    return f"Note #'{note_id}': text added."


@input_error
def remove_tag(args, notes_engine):
    if len(args) < 2:
        raise InvalidArgsError
    try:
        note_id = int(args[0])
    except ValueError as e:
        raise InvalidIdValueError from e

    tag = "".join(args[1])

    notes_engine.remove_tag(note_id, tag)
    return f"Note #'{id}': tag: {tag} removed."


@input_error
def notes(notes_engine):
    return notes_engine.get_all_notes()


@input_error
def find_note(args, notes_engine):
    if len(args) != 1:
        raise InvalidArgsError
    symbols = args[0]

    if len(symbols) < 2:
        raise InvalidSearchPatternError

    result = notes_engine.find_note(symbols)
    if result:
        return result
    return "Nothing was found for the specified string."
