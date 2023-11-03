from modules.bot_assistant.models.exceptions import (
    InvalidArgsError,
    InvalidSearchPatternError,
)
from modules.bot_assistant.decorators.decorators import input_error, validate_id


@input_error
def add_note(args, notes_engine):
    if len(args) < 1:
        raise InvalidArgsError
    title = " ".join(args[0:])
    num = notes_engine.add_note(title)
    return f"Note #'{num}' added."


@input_error
@validate_id
def add_tag(args, noteslist):
    if len(args) != 2:
        raise InvalidArgsError

    note_id = int(args[0])
    tag = args[1]

    noteslist.add_tag(note_id, tag)
    return f"Note #'{note_id}': tag '{tag}' added."


@input_error
@validate_id
def change_status(args, notes_engine):
    if len(args) != 2:
        raise InvalidArgsError

    note_id = int(args[0])
    status = args[1]

    notes_engine.change_status(note_id, status)
    return f"Note #'{note_id}': status changed to '{status}'."


@input_error
@validate_id
def remove_note(args, notes_engine):
    if len(args) != 1:
        raise InvalidArgsError

    note_id = int(args[0])

    notes_engine.remove_note(note_id)
    return f"Note #'{note_id}' deleted"


@input_error
@validate_id
def edit_title(args, notes_engine):
    if len(args) < 2:
        raise InvalidArgsError

    note_id = int(args[0])
    title = " ".join(args[1:])

    notes_engine.edit_title(note_id, title)
    return f"Note #'{note_id}': title edited."


@input_error
@validate_id
def add_text(args, notes_engine):
    if len(args) < 2:
        raise InvalidArgsError

    note_id = int(args[0])
    text = " ".join(args[1:])

    notes_engine.add_text(note_id, text)
    return f"Note #'{note_id}': text added."


@input_error
@validate_id
def remove_tag(args, notes_engine):
    if len(args) < 2:
        raise InvalidArgsError

    note_id = int(args[0])
    tag = "".join(args[1])

    notes_engine.remove_tag(note_id, tag)
    return f"Note #'{id}': tag: {tag} removed."


@input_error
def notes(notes_engine):
    return notes_engine.get_all_notes()


@input_error
@validate_id
def show_note(args, notes_engine):
    if len(args) != 1:
        raise InvalidArgsError

    note_id = int(args[0])

    return notes_engine.show_note(note_id)


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
