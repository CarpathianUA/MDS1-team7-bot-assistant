import sys
import modules.bot_assistant.models.exceptions as exceptions
from modules.bot_assistant.models.notes import Note, Tag, Text
from modules.bot_assistant.decorators.decorators import input_error


@input_error
def add_note(args, notes):
    if len(args) < 1:
        raise exceptions.InvalidArgsError
    title = " ".join(args[0:])

    note = Note(title)
    notes.add_note(note)
    return f"Note '{note}' added."


@input_error
def add_tag(args, notes):
    if len(args) != 1:
        raise exceptions.InvalidArgsError
    tag = args

    if tag not in notes:
        notes.add_tag(Tag(tag))
        return f"Tag '{tag}' added."
    else:
        raise exceptions.TagAlreadyExistsError


@input_error
def delete_note(args, notes):
    pass


@input_error
def edit_title(args, notes):
    pass


@input_error
def add_text(args, notes):
    if len(args) > 1:
        raise exceptions.InvalidArgsError
    text = " ".join(args[0:])

    txt = Text(text)
    notes.add_text(txt)
    return f"Text added."


@input_error
def edit_text(args, notes):
    pass


@input_error
def remove_tag(args, notes):
    pass


@input_error
def get_all_notes(notes):
    return notes.get_all_notes()


@input_error
def find_note(args, notes):
    if len(args) != 1:
        raise exceptions.InvalidArgsError
    symbols = args[0]

    if len(symbols) < 2:
        raise exceptions.InvalidSearchPatternError

    result = notes.find_note(symbols)
    if result:
        return result
    return "Nothing was found for the specified string."


@input_error
def find_note_by_filter(args, notes):
    pass
