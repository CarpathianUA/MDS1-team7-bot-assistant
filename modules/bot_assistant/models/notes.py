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
    NoteIdAlreadyExistsError,
    NoteDoesNotExistError,
    TagAlreadyExistsError,
    TagDoesNotExistsError,
    InvalidTagLengthError,
)
from modules.bot_assistant.utils.color_fillers import fill_background_color
from modules.bot_assistant.utils.format_note import format_note, format_note_with_tags
from modules.bot_assistant.utils.state import is_valid_state
from modules.bot_assistant.models.note_state import State
from modules.bot_assistant.constants.file_paths import NOTES_FILE, DATA_STORAGE_DIR
from modules.bot_assistant.constants.notes_params import TITLE_LEN, TAG_LEN, TEXT_LEN
from modules.bot_assistant.constants.date_formats import NOTES_DATE_FORMAT
from modules.bot_assistant.constants.note_formatting import TITLE


class Title(Field):
    def __init__(self, value):
        if self.__is_valid(value):
            super().__init__(value)
            self._value = None
            self.value = value
        else:
            raise InvalidTitleLengthError

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

    @staticmethod
    def __is_valid(value):
        return TITLE_LEN >= len(value) > 0


class Tag(Field):
    def __init__(self, value):
        if self.__is_valid(value):
            super().__init__(value)
            self._value = None
            self.value = value
        else:
            raise InvalidTagLengthError

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

    @staticmethod
    def __is_valid(value):
        return TAG_LEN >= len(value) > 0


class Text(Field):
    def __init__(self, value):
        if self.__is_valid(value):
            super().__init__(value)
            self._value = None
            self.value = value
        raise InvalidTextLengthError

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

    @staticmethod
    def __is_valid(value):
        return TEXT_LEN >= len(value) > 0


class Date(Field):
    def __init__(self):
        value = datetime.datetime.now().strftime(NOTES_DATE_FORMAT)
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
    def __init__(self, note_id, title):
        self.id = note_id
        self.title = Title(title)
        self.text = ""
        self.creation_date = Date()
        self.edited = Field("")
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
            self.text += f" {text}"
            self.edited = Date()
            return
        self.text = text

    def override_text(self, text):
        self.text = text
        self.edited = Date()

    def __hash__(self):
        return hash(self)

    def __eq__(self, other):
        return self == other

    def __str__(self):
        return format_note(self)


class Notes(UserDict):
    # for quick access to a specific note
    note_counter = 0

    def add_note(self, title):
        self.note_counter += 1
        if self.__is_key_exist(self.note_counter):
            raise NoteIdAlreadyExistsError
        note = Note(self.note_counter, title)
        self.data[self.note_counter] = note
        return self.note_counter

    def edit_title(self, note_id: int, title):
        if self.__is_key_exist(note_id):
            self.data[note_id].edit_title(title)
        else:
            raise NoteIdAlreadyExistsError

    def add_tag(self, note_id: int, tag):
        if self.__is_key_exist(note_id):
            self.data[note_id].add_tag(Tag(tag))
        else:
            raise NoteDoesNotExistError

    def remove_tag(self, note_id: int, tag):
        if self.__is_key_exist(note_id):
            self.data[note_id].remove_tag(Tag(tag))
        else:
            raise NoteDoesNotExistError

    def add_text(self, note_id: int, text):
        if self.__is_key_exist(note_id):
            self.data[note_id].add_text(text)
        else:
            raise NoteDoesNotExistError

    def override_text(self, note_id: int, text):
        if self.__is_key_exist(note_id):
            self.data[note_id].override_text(text)
        else:
            raise NoteDoesNotExistError

    def change_status(self, note_id: int, status):
        if self.__is_key_exist(note_id):
            self.data[note_id].change_status(status)
        else:
            raise NoteDoesNotExistError

    def find_note(self, symbols):
        result = ""
        for note in self.data.values():
            occurrence = regex.findall(str.lower(symbols), str.lower(str(note)))
            if any(occurrence):
                result += f"{fill_background_color(format_note(note), symbols)}\n"

        if result:
            return TITLE + result
        return "Nothing was found for the specified symbols."

    def find_notes_by_tag(self, tag):
        result = ""
        for note in self.data.values():
            if note.tags and Tag(tag) in note.tags:
                # move searchable tag to the first position
                filtered_tags = (
                    str(tag)
                    + "; "
                    + "; ".join([p.value for p in note.tags if p != Tag(tag)])
                )
                tags = fill_background_color(filtered_tags, str(tag))
                result += f"{format_note_with_tags(note, tags)}\n"

        if result:
            return TITLE + result
        return "Nothing was found for the specified tag."

    def remove_note(self, note_id: int):
        if not self.__is_key_exist(note_id):
            raise NoteDoesNotExistError
        self.data.pop(note_id, None)

    def get_all_notes(self):
        if any(self.data):
            return TITLE + str(self)
        return "You don’t have any notes"

    def show_note(self, note_id):
        if not self.__is_key_exist(note_id):
            raise NoteDoesNotExistError
        return TITLE + str(self.data[note_id])

    def save_to_file(self):
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
        # Define the path to the file
        home_dir = os.path.expanduser("~")
        notes_dir = os.path.join(home_dir, DATA_STORAGE_DIR)
        notes_path = os.path.join(notes_dir, NOTES_FILE)

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
