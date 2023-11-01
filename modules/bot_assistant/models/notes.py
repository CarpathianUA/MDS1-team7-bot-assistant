import os
import pickle
import datetime
import re as regex
from collections import UserDict
from constants.date_format import DATE_FORMAT
from modules.bot_assistant.models.field import Field
from modules.bot_assistant.models.exceptions import (
    InvalidTitleLengthError,
    InvalidTextLengthError,
    InvalidNoteStatusError,
    TitleDoesNotExistError,
)
from modules.bot_assistant.utils.color_fillers import fill_background_color
from modules.bot_assistant.utils.note_state import State, is_valid_state
from modules.bot_assistant.constants.file_paths import NOTES_FILE
from modules.bot_assistant.constants.notes_params import TITLE_LEN, TEXT_LEN


class Title(Field):
    def __init__(self, value):
        super().__init__(value)
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if self.__is_valid(value):
            self._value = value
        raise InvalidTitleLengthError

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

    @staticmethod
    def __is_valid(value):
        return len(value) <= TITLE_LEN and len(value) > 0


class Tag(Field):
    def __init__(self, value):
        super().__init__(value)
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value


class Text(Field):
    def __init__(self, value):
        super().__init__(value)
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if self.__is_valid(value):
            self._value = value
        raise InvalidTextLengthError

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

    @staticmethod
    def __is_valid(value):
        return len(value) <= TEXT_LEN and len(value) > 0


class Date(Field):
    def __init__(self):
        super().__init__(datetime.datetime.now().strftime(DATE_FORMAT))

    @property
    def value(self):
        return super().value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return f"{self.value.strftime(DATE_FORMAT)}"


class Status(Field):
    def __init__(self):
        value = State.NOTSTARTED
        super().__init__(value)
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if is_valid_state(value):
            self._value = State[value]
        raise InvalidNoteStatusError

    def __str__(self):
        return f"{self.value}"


class Note:
    def __init__(self, title):
        self.title = Title(title)
        self.text = ""
        self.creation_date = Date()
        self.edited = None
        self.status = Status()
        self.tags = []

    def edit_title(self, title):
        self.title = Title(title)
        self.edited = Date()

    def change_status(self, status):
        self.status.value = status
        self.edited = Date()

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def edit_text(self, text):
        self.text = text
        self.edited = Date()

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        tags_str = (
            "; ".join(p.value for p in self.tags) if self.tags else "No tags available"
        )
        return f"Note: title:{self.title} tags: {tags_str}, creatin date: {self.creation_date}, edited: {self.edited}, status: {self.status}, text: {self.text}\n"


class Notes(UserDict):
    # for quick access to a specific note
    note_counter = 0

    def __is_key_exist(self, key):
        return key in self.data

    def add_note(self, note: Note):
        Notes.note_counter += 1
        self.data[Notes.note_counter] = note

    def find_note(self, symbols):
        result = ""
        for note in self.data.values():
            occurrence = regex.findall(symbols, str(note))
            if any(occurrence):
                result += f"{fill_background_color(str(note), symbols)}\n"

        return result

    # TODO: add filter
    def find_note_by_filter(self, symbols, filter):
        pass

    def delete(self, title):
        if not self.__is_key_exist(title):
            raise TitleDoesNotExistError
        self.data.pop(title, None)
        return f"Note '{title}' has been deleted."

    def get_all_notes(self):
        return self.data

    def save_to_file(self):
        with open(NOTES_FILE, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def load_from_file(cls):
        if os.path.exists(NOTES_FILE):
            with open(NOTES_FILE, "rb") as f:
                return pickle.load(f)
        return cls()

    def __str__(self):
        return "\n".join(str(note) for note in self.data.values())
