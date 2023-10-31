import os
import pickle
import datetime
import re as regex
from collections import UserDict
from field import Field
from utils.note_status import Status, is_valid_status
from constants.date_format import DATE_FORMAT
from modules.bot_assistant.models.exceptions import (
    InvalidNoteStatusError,
    TitleDoesNotExistError
)
from modules.bot_assistant.utils.color_fillers import fill_background_color
from modules.bot_assistant.constants.file_paths import NOTES_FILE

class Title(Field):
    def __hash__(self):
        return hash(self.value)
    
    def __eq__(self, other):
        return self.value == other.value
    

class Tag(Field):
    def __hash__(self):
        return hash(self.value)
    
    def __eq__(self, other):
        return self.value == other.value


class Text(Field):
    def __hash__(self):
        return hash(self.value)
    
    def __eq__(self, other):
        return self.value == other.value


class Date(Field):
    def __init__(self):
        super().__init__(datetime.datetime.now().strftime(DATE_FORMAT))

    def __hash__(self):
        return hash(self.value)
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __str__(self):
        return f"{self.value.strftime(DATE_FORMAT)}"


class Status(Field):
    def __init__(self):
        super().__init__(Status.NOTSTARTED)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if is_valid_status(value):
            self._value = Status[value]
        raise InvalidNoteStatusError
    
    def __str__(self):
        return f"{self.value}"


class Note:
    def __init__(self, title):
        self.title = Title(title)
        self.text = ""
        self.date = Date()
        self.status = Status()
        self.tags = []

    def edit_title(self, title):
        self.title = Title(title)

    def change_status(self, status):
        self.status.value = status

    def add_tag(self, tag):
        if Tag(tag) not in self.tags:
            self.tags.append(Tag(tag))

    def edit_text(self, text):
        self.text = text

    def __hash__(self):
        return hash(self.value)
    
    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        tags_str = (
            "; ".join(p.value for p in self.tags)
            if self.tags
            else "No tags available"
        )
        return f"Note: title:{self.title} tags: {tags_str}, creatin date: {self.date}, status: {self.status}, text: {self.text}\n"


class Notes(UserDict):
        def __is_key_exist(self, key):
            return key in self.data

        def add_record(self, Note):
            self.data[Note.title.value] = Note

        def find_note(self, symbols):
            result = ""
            for note in self.data.values():
                occurrence = regex.findall(symbols, str(note))
                if any(occurrence):
                    result += f"{fill_background_color(str(note), symbols)}\n"

            return result
        
        #TODO: add filter 
        def find_note_by_filter(self, symbols, filter):
            pass
        
        def delete(self, title):
            if not self.__is_key_exist(title):
                raise TitleDoesNotExistError
            self.data.pop(title, None)
            return f"Note '{title}' has been deleted."
        
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
