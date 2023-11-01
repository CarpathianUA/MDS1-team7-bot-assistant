import modules.bot_assistant.models.exceptions as exceptions
from modules.bot_assistant.constants.periods_ranges import DEFAULT_PERIOD
from modules.bot_assistant.decorators.decorators import input_error
from modules.bot_assistant.models.address_book import Record


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
def edit_contact(args, address_book):
    if len(args) != 2:
        raise exceptions.InvalidArgsError
    old_name, new_name = args

    if old_name in address_book.data:
        record = address_book.data.pop(old_name)
        record.name.value = new_name
        address_book.data[new_name] = record
        return f"Contact's name {old_name} changed to a new one: {new_name}."
    else:
        raise exceptions.ContactDoesNotExistError


@input_error
def add_phone(args, address_book):
    if len(args) != 2:
        raise exceptions.InvalidArgsError
    name, phone = args

    if name in address_book:
        record = address_book.data[name]
        record.add_phone(phone)
        return f"Phone {phone} has been added to contact {name}."
    else:
        raise exceptions.ContactDoesNotExistError


@input_error
def edit_phone(args, address_book):
    if len(args) != 3:
        raise exceptions.InvalidArgsError
    name, phone, new_phone = args

    if name in address_book:
        record = address_book.data[name]
        record.edit_phone(phone, new_phone)
        return f"Contact {name} phone changed to a new one: {new_phone}."
    else:
        raise exceptions.PhoneDoesNotExistError


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
def add_email(args, address_book):
    if len(args) != 2:
        raise exceptions.InvalidArgsError
    name, email = args

    if name in address_book:
        record = address_book.data[name]
        record.add_email(email)
        return f"Email {email} has been added to contact {name}."
    else:
        raise exceptions.ContactDoesNotExistError


@input_error
def edit_email(args, address_book):
    if len(args) != 3:
        raise exceptions.InvalidArgsError
    name, email, new_email = args

    if name in address_book:
        record = address_book.data[name]
        record.edit_email(email, new_email)
        return f"Contact`s {name} email changed to a new one: {new_email}."
    else:
        raise exceptions.PhoneDoesNotExistError


@input_error
def get_contact_email(args, address_book):
    if len(args) != 1:
        raise exceptions.InvalidArgsError
    name = args[0]

    if name in address_book:
        record = address_book.data[name]
        emails = [email.value for email in record.emails]
        return f"Email: {', '.join(emails)}"
    else:
        raise exceptions.ContactDoesNotExistError


@input_error
def remove_email(args, address_book):
    if len(args) != 2:
        raise exceptions.InvalidArgsError

    name, email = args

    record = address_book.data.get(name)
    if not record:
        raise exceptions.ContactDoesNotExistError

    if record.find_email(email):
        record.remove_email(email)
        return f"Email {email} removed from {name}."
    else:
        raise exceptions.EmailDoesNotExistError
    
   
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
def remove_birthday(args, address_book):
    if len(args) != 2:
        raise exceptions.InvalidArgsError

    name, birthday = args

    record = address_book.data.get(name)
    if not record:
        raise exceptions.ContactDoesNotExistError

    if record.birthday and record.birthday.value == birthday:
        record.birthday.value = None
        return f"Birthday {birthday} removed from {name}."
    else:
        raise exceptions.ContactWithThisBirthdayDoesNotExist


@input_error
def show_birthday(args, address_book):
    if len(args) != 1:
        raise exceptions.InvalidArgsError
    name = args[0]

    if name in address_book:
        record = address_book.data[name]
        if record.birthday.value:
            return f"{name}'s birthday: {record.birthday.value}"
    else:
        raise exceptions.ContactDoesNotExistError


@input_error
def find_contact(args, address_book):
    if len(args) != 1:
        raise exceptions.InvalidArgsError
    symbols = args[0]

    if len(symbols) < 2:
        raise exceptions.InvalidSearchPatternError

    result = address_book.find_record(symbols)
    if result:
        return result
    return "Nothing was found for the specified string."


@input_error
def show_birthdays_per_period(args, address_book):
    if not args:
        days = DEFAULT_PERIOD
    else:
        try:
            days = int(args[0])
            if days <= 0:
                return "Please enter a positive number of days."
        except ValueError:
            return "Please enter a valid number."

    birthdays = address_book.get_birthdays_per_period(days)

    if not birthdays:
        return "No birthdays in the upcoming period."

    result = f"Birthdays in the upcoming {days} days:\n"
    for day, contacts in birthdays.items():
        contacts_str = ", ".join(
            f"{name} ({birthday_date})" for name, birthday_date in contacts
        )
        result += f"{day}: {contacts_str}\n"

    return result
