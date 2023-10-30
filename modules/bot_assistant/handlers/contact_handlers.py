from modules.bot_assistant.decorators.decorators import input_error
from modules.bot_assistant.models.address_book import Record
import modules.bot_assistant.models.exceptions as exceptions


def hello(address_book):
    return f"Hello! You have {len(address_book)} contacts in your address book. How can I help you?"


@input_error
def add_contact(args, address_book):
    if len(args) != 2:
        raise exceptions.InvalidArgsError
    name, phone = args

    if name not in address_book:
        record = Record(name)
        record.add_phone(phone)
        address_book.add_record(record)
        return f"Contact {name} added."
    else:
        raise exceptions.ContactAlreadyExistsError


@input_error
def change_contact(args, address_book):
    if len(args) != 2:
        raise exceptions.InvalidArgsError
    name, phone = args

    if name in address_book:
        record = address_book.data[name]
        record.add_phone(phone)
        return f"Contact {name} changed."
    else:
        raise exceptions.ContactDoesNotExistError


@input_error
def get_contact_phone(args, address_book):
    if len(args) != 1:
        raise exceptions.InvalidArgsError
    name = args[0]

    if name in address_book:
        record = address_book.data[name]
        phones = [phone.value for phone in record.phones]
        return f"Phone: {', '.join(phones)}"
    else:
        raise exceptions.ContactDoesNotExistError


@input_error
def remove_phone(args, address_book):
    if len(args) != 2:
        raise exceptions.InvalidArgsError

    name, phone = args

    record = address_book.data.get(name)
    if not record:
        raise exceptions.ContactDoesNotExistError

    if record.find_phone(phone):
        record.remove_phone(phone)
        return f"Phone {phone} removed from {name}."
    else:
        raise exceptions.PhoneDoesNotExistError


@input_error
def delete_contact(args, address_book):
    if len(args) != 1:
        raise exceptions.InvalidArgsError
    name = args[0]

    if name in address_book:
        address_book.pop(name)
        return f"Contact {name} deleted."
    else:
        raise exceptions.ContactDoesNotExistError


def get_all_contacts(address_book):
    if not address_book:
        return "You don't have any contacts."
    return "\n".join(str(record) for record in address_book.data.values())


@input_error
def add_birthday(args, address_book):
    if len(args) != 2:
        raise exceptions.InvalidArgsError
    name, birthday = args

    if name in address_book:
        record = address_book.data[name]
        record.add_birthday(birthday)
        return f"Birthday for {name} added."
    else:
        raise exceptions.ContactDoesNotExistError


@input_error
def show_birthday(args, address_book):
    if len(args) != 1:
        raise exceptions.InvalidArgsError
    name = args[0]

    if name in address_book:
        record = address_book.data[name]
        if record.birthday.value:
            return f"{name}'s birthday: {record.birthday}"
    else:
        raise exceptions.ContactDoesNotExistError


def show_birthdays_per_week(address_book):
    birthdays = address_book.get_birthdays_per_week()

    if not birthdays:
        return "No birthdays in the upcoming week."

    result = ""
    if "Today" in birthdays:
        result += "Birthdays today:\n"
        result += f"Today: {', '.join(birthdays.pop('Today'))} 🎉\n"

    if birthdays:
        result += "Birthdays in the upcoming week:\n"
        for day, names in birthdays.items():
            result += f"{day}: {', '.join(names)}\n"

    return result
