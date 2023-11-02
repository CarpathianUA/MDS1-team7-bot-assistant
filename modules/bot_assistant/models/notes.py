import os
import pickle
import datetime
import re as regex
from collections import UserDict
from modules.bot_assistant.models.field import Field
from modules.bot_assistant.models.exceptions import (
    InvalidTitleLengthError,
    InvalidTextLengthError,
    InvalidNoteStatusError,
    NoteIdAlreadyExisrsError,
    NoteDoesNotExistError,
    TagAlreadyExistsError,
    TagDoesNotExistsError,
)
from modules.bot_assistant.utils.color_fillers import fill_background_color
from modules.bot_assistant.models.note_state import State, is_valid_state
from modules.bot_assistant.constants.file_paths import NOTES_FILE, DATA_STORAGE_DIR
from modules.bot_assistant.constants.notes_params import TITLE_LEN, TEXT_LEN
from modules.bot_assistant.constants.date_format import DATE_FORMAT


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
        else:
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
        return self._value == other.value

    def __str__(self):
        return f"{self._value}"


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
        value = datetime.datetime.now().strftime(DATE_FORMAT)
        super().__init__(value)
        self._value = value

    def __hash__(self):
        return hash(self._value)

    def __eq__(self, other):
        return self._value == other.value

    def __str__(self):
        return f"{self._value}"


class Status(Field):
    def __init__(self):
        value = State.NOT_STARTED
        super().__init__(value)
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if is_valid_state(value):
            self._value = value
        else:
            raise InvalidNoteStatusError

    def __str__(self):
        return f"{self.value}"


class Note:
    def __init__(self, id, title):
        self.id = id
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
        if is_valid_state(status):
            self.status.value = State[status.upper()]
            self.edited = Date()
        else:
            raise InvalidNoteStatusError

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)
        else:
            raise TagAlreadyExistsError

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)
        else:
            raise TagDoesNotExistsError

    def add_text(self, text):
        if any(self.text):
            self.edited = Date()
        self.text = text

    def __hash__(self):
        return hash(self)

    def __eq__(self, other):
        return self == other

    def __str__(self):
        tags_str = (
            "; ".join(p.value for p in self.tags) if self.tags else "No tags available"
        )
        return f"Note #'{self.id}', title: '{self.title}', tags: {tags_str}, creation date: {self.creation_date}, edited: {self.edited}, status: '{self.status}', text: {self.text}\n"


class Notes(UserDict):
    # for quick access to a specific note
    note_counter = 0

    def add_note(self, title):
        self.note_counter += 1
        if self.__is_key_exist(self.note_counter):
            raise NoteIdAlreadyExisrsError
        note = Note(self.note_counter, title)
        self.data[self.note_counter] = note
        return self.note_counter

    def edit_title(self, id: int, title):
        if self.__is_key_exist(id):
            self.data[id].edit_title(title)
        else:
            raise NoteIdAlreadyExisrsError

    def add_tag(self, id: int, tag):
        if self.__is_key_exist(id):
            self.data[id].add_tag(Tag(tag))
        else:
            raise NoteDoesNotExistError

    def remove_tag(self, id: int, tag):
        if self.__is_key_exist(id):
            self.data[id].remove_tag(Tag(tag))
        else:
            raise NoteDoesNotExistError

    def add_text(self, id: int, text):
        if self.__is_key_exist(id):
            self.data[id].add_text(text)
        else:
            raise NoteDoesNotExistError

    def change_status(self, id: int, status):
        if self.__is_key_exist(id):
            self.data[id].change_status(status)
        else:
            raise NoteDoesNotExistError

    def find_note(self, symbols):
        result = ""
        for note in self.data.values():
            occurrence = regex.findall(str.lower(symbols), str.lower(str(note)))
            if any(occurrence):
                result += f"{fill_background_color(str(note), symbols)}\n"

        return result

    def remove_note(self, id: int):
        """Function removes note from notes."""

        if not self.__is_key_exist(id):
            raise NoteDoesNotExistError
        self.data.pop(id, None)

    def get_all_notes(self):
        """Function returns notes in str()."""

        return self

    def save_to_file(self):
        """Function save data to file."""

        # We store data state to user's home directory
        home_dir = os.path.expanduser("~")
        notes_dir = os.path.join(
            home_dir, DATA_STORAGE_DIR
        )  # Hidden directory in home folder, where we store the file
        os.makedirs(notes_dir, exist_ok=True)

        # Define the path to the file within the directory
        notes_path = os.path.join(notes_dir, NOTES_FILE)

        with open(notes_path, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def load_from_file(cls):
        """Function loads file."""

        # Define the path to the file
        home_dir = os.path.expanduser("~")
        notes_dir = os.path.join(home_dir, DATA_STORAGE_DIR)
        notes_path = os.path.join(notes_dir, NOTES_FILE)

        # Load the file if it exists
        if os.path.exists(notes_path):
            with open(notes_path, "rb") as f:
                return pickle.load(f)
        return cls()

    def __is_key_exist(self, key):
        return key in self.data.keys()

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["note_counter"] = self.note_counter
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value

    def __str__(self):
        return "\n".join(str(note) for note in self.data.values())
