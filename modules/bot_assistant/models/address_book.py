import os
import pickle
import re as regex
from collections import UserDict, defaultdict
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from modules.bot_assistant.constants.file_paths import ADDRESS_BOOK_FILE
from modules.bot_assistant.constants.periods_ranges import MAX_PERIOD, PERIODS
from modules.bot_assistant.models.exceptions import (
    InvalidPhoneError,
    InvalidBirthdayFormatError,
    InvalidBirthdayRangeError,
    ContactDoesNotExistError,
    InvalidEmailError,
)
from modules.bot_assistant.utils.birthdays import is_valid_birth_date
from modules.bot_assistant.utils.phone_numbers import is_valid_phone
from modules.bot_assistant.utils.emails import is_valid_email
from modules.bot_assistant.utils.color_fillers import fill_background_color


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not self._validate_phone(value):
            raise InvalidPhoneError
        self._value = value

    @staticmethod
    def _validate_phone(phone):
        return is_valid_phone(phone)
    
class Address(Field):
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

class Email(Field):
    def __init__(self, value):
        super().__init__(value)
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not self._validate_email(value):
            raise InvalidEmailError
        self._value = value

    @staticmethod
    def _validate_email(email):
        return is_valid_email(email)


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value is not None and not self._validate_birthday(value):
            raise InvalidBirthdayFormatError
        self._value = value

    @staticmethod
    def _validate_birthday(birthday):
        return is_valid_birth_date(birthday)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = list()
        self.emails = list()
        self.birthday = Birthday(None)
        self.addresses = list()

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, phone, new_phone):
        for p in self.phones:
            if p.value == phone:
                p.value = new_phone

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def add_address(self, address):
        self.addresses.append(Address(address))

    def edit_address(self, address, new_address):
        for p in self.addresses:
            if p.value == address:
                p.value = new_address

    def find_address(self, address):
        for p in self.addresses:
            if p.value == address:
                return p

    def remove_address(self, address):
        self.addresses = [p for p in self.addresses if p.value != address]
    
    def add_email(self, email):
        self.emails.append(Email(email))

    def edit_email(self, email, new_email):
        for e in self.emails:
            if e.value == email:
                e.value = new_email

    def find_email(self, email):
        for e in self.emails:
            if e.value == email:
                return e

    def remove_email(self, email):
        self.emails = [e for e in self.emails if e.value != email]

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def get_birthday(self):
        if self.birthday and self.birthday.value:
            return self.birthday.value

    def __str__(self):
        phones_str = (
            "; ".join(p.value for p in self.phones)
            if self.phones
            else "No phones available"
        )
        emails_str = (
            "; ".join(e.value for e in self.emails)
            if self.emails
            else "No emails available"
        )
        birthday_str = (
            self.birthday.value
            if self.birthday and self.birthday.value
            else "No birthday available"
        )

        address_str = (
            "; ".join(p.value for p in self.addresses)
            if self.addresses
            else "No address available"
        )
        return f"Contact name: {self.name.value}, phones: {phones_str}, birthday: {birthday_str}, emails: {emails_str}, addresses: {address_str}"


class AddressBook(UserDict):
    def __is_key_exist(self, key):
        return key in self.data

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if not self.__is_key_exist(name):
            raise ContactDoesNotExistError
        return self.data[name]

    def find_record(self, symbols):
        result = ""
        for record in self.data.values():
            occurrence = regex.findall(symbols, str(record))
            if any(occurrence):
                result += f"{fill_background_color(str(record), symbols)}\n"

        return result

    def delete(self, name):
        if not self.__is_key_exist(name):
            raise ContactDoesNotExistError
        self.data.pop(name, None)
        return f"Contact '{name}' has been deleted."

    def process_record_for_birthday(self, record, today, birthdays, end_date):
        name = record.name.value
        birthday_date = self.get_upcoming_birthday(record, today)
        if birthday_date is None or birthday_date < today or birthday_date > end_date:
            return None

        day_to_say_happy_birthday = self.calculate_birthday_wish_day(
            birthday_date, today
        )
        if day_to_say_happy_birthday:
            birthdays[day_to_say_happy_birthday].append(
                (name, birthday_date.strftime("%d.%m.%Y"))
            )

    def get_birthdays_per_period(self, days):
        if days > MAX_PERIOD:
            raise InvalidBirthdayRangeError
        today = datetime.today().date()
        end_date = today + timedelta(days=days)
        birthdays = defaultdict(list)

        for record in self.data.values():
            self.process_record_for_birthday(record, today, birthdays, end_date)

        return birthdays

    @staticmethod
    def calculate_birthday_wish_day(birthday_date, today):
        delta = relativedelta(birthday_date, today)

        for period, label, unit in PERIODS:
            if unit == "days":
                if (birthday_date - today).days < period:
                    return label
            elif unit == "months":
                # calculate the total number of months between two dates based on their relative difference
                total_months = delta.years * 12 + delta.months
                if total_months < period:
                    return label

        return None

    @staticmethod
    def get_upcoming_birthday(record, today):
        if not record.birthday or not record.birthday.value:
            return None

        birthday_str = record.birthday.value
        birthday_date = datetime.strptime(birthday_str, "%d.%m.%Y").date()
        birthday_date = birthday_date.replace(year=today.year)

        if birthday_date < today:
            birthday_date = birthday_date.replace(year=today.year + 1)

        return birthday_date

    def save_to_file(self):
        with open(ADDRESS_BOOK_FILE, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def load_from_file(cls):
        if os.path.exists(ADDRESS_BOOK_FILE):
            with open(ADDRESS_BOOK_FILE, "rb") as f:
                return pickle.load(f)
        return cls()

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
