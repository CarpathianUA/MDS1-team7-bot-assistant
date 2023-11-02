import modules.bot_assistant.models.exceptions as exceptions
from modules.bot_assistant.constants.periods_ranges import DEFAULT_PERIOD
from modules.bot_assistant.decorators.decorators import input_error, contact_exists
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
@contact_exists
def edit_contact(args, address_book):
    if len(args) != 2:
        raise exceptions.InvalidArgsError
    old_name, new_name = args

    if old_name in address_book.data:
        record = address_book.data.pop(old_name)
        record.name.value = new_name
        address_book.data[new_name] = record
        return f"Contact's name {old_name} changed to a new one: {new_name}."


@input_error
@contact_exists
def add_phone(args, address_book):
    if len(args) != 2:
        raise exceptions.InvalidArgsError
    name, phone = args

    record = address_book.data[name]

    if record.find_phone(phone):
        raise exceptions.PhoneAlreadyExistsError
    record.add_phone(phone)
    return f"Phone {phone} has been added to contact {name}."


@input_error
@contact_exists
def edit_phone(args, address_book):
    if len(args) != 3:
        raise exceptions.InvalidArgsError
    name, phone, new_phone = args

    record = address_book.data[name]

    if record.find_phone(phone):
        record.edit_phone(phone, new_phone)
        return f"Contact {name} phone changed to a new one: {new_phone}."
    else:
        raise exceptions.PhoneDoesNotExistError


@input_error
@contact_exists
def get_contact_phone(args, address_book):
    if len(args) != 1:
        raise exceptions.InvalidArgsError
    name = args[0]

    if name in address_book:
        record = address_book.data[name]
        phones = [phone.value for phone in record.phones]
        return f"Phone: {', '.join(phones)}"


@input_error
@contact_exists
def remove_phone(args, address_book):
    if len(args) != 2:
        raise exceptions.InvalidArgsError
    name, phone = args

    record = address_book.data[name]

    if record.find_phone(phone):
        record.remove_phone(phone)
        return f"Phone {phone} removed from {name}."
    else:
        raise exceptions.PhoneDoesNotExistError


@input_error
@contact_exists
def add_address(args, address_book):
    if len(args) < 2:
        raise exceptions.InvalidArgsError

    name = args.pop(0)
    address_str = ""
    for arg in args:
        if not address_str:
            address_str += arg
        else:
            address_str += " " + arg

    address = address_str

    record = address_book.data[name]

    if record.find_address(address):
        raise exceptions.AddressAlreadyExistsError
    record.add_address(address)
    return f"Address {address} has been added to contact {name}."


@input_error
@contact_exists
def edit_address(args, address_book):
    if len(args) < 3:
        raise exceptions.InvalidArgsError

    name = args.pop(0)
    address_str = ""
    for arg in args:
        if not address_str:
            address_str += arg
        else:
            address_str += " " + arg
    addresses_list = [element.strip() for element in address_str.split(";")]

    if len(addresses_list) != 2:
        raise exceptions.InvalidArgsError
    else:
        address = addresses_list[0].strip()
        new_address = addresses_list[1].strip()

    record = address_book.data[name]

    if not record.find_address(address):
        raise exceptions.AddressDoesNotExistError
    record.edit_address(address, new_address)
    return f"Address for {name} changed to a new one: {new_address}."


@input_error
@contact_exists
def get_contact_address(args, address_book):
    if len(args) != 1:
        raise exceptions.InvalidArgsError
    name = args[0]

    if name in address_book:
        record = address_book.data[name]
        addresses = [address.value for address in record.addresses]
        return f"{name}'s address(es): {', '.join(addresses)}"


@input_error
@contact_exists
def remove_address(args, address_book):
    if len(args) < 2:
        raise exceptions.InvalidArgsError

    name = args.pop(0)
    address_str = ""
    for arg in args:
        if not address_str:
            address_str += arg
        else:
            address_str += " " + arg
    address = address_str

    record = address_book.data[name]

    if record.find_address(address):
        record.remove_address(address)
        return f"Address {address} removed from {name}."
    else:
        raise exceptions.AddressDoesNotExistError


@input_error
@contact_exists
def add_email(args, address_book):
    if len(args) != 2:
        raise exceptions.InvalidArgsError
    name, email = args

    record = address_book.data[name]

    if record.find_email(email):
        raise exceptions.EmailAlreadyExistsError
    record.add_email(email)
    return f"Email {email} has been added to contact {name}."


@input_error
@contact_exists
def edit_email(args, address_book):
    if len(args) != 3:
        raise exceptions.InvalidArgsError
    name, email, new_email = args

    record = address_book.data[name]

    if record.find_email(email):
        record.edit_email(email, new_email)
        return f"Email for {name} changed to a new one: {new_email}."
    else:
        raise exceptions.EmailDoesNotExistError


@input_error
@contact_exists
def get_contact_email(args, address_book):
    if len(args) != 1:
        raise exceptions.InvalidArgsError
    name = args[0]

    if name in address_book:
        record = address_book.data[name]
        emails = [email.value for email in record.emails]
        return f"Email: {', '.join(emails)}"


@input_error
@contact_exists
def remove_email(args, address_book):
    if len(args) != 2:
        raise exceptions.InvalidArgsError
    name, email = args

    record = address_book.data[name]

    if record.find_email(email):
        record.remove_email(email)
        return f"Email {email} removed from {name}."
    else:
        raise exceptions.EmailDoesNotExistError


@input_error
@contact_exists
def delete_contact(args, address_book):
    if len(args) != 1:
        raise exceptions.InvalidArgsError
    name = args[0]

    if name in address_book:
        address_book.pop(name)
        return f"Contact {name} deleted."


def get_all_contacts(address_book):
    if not address_book:
        return "You don't have any contacts."
    return "\n".join(str(record) for record in address_book.data.values())


@input_error
@contact_exists
def add_birthday(args, address_book):
    if len(args) != 2:
        raise exceptions.InvalidArgsError
    name, birthday = args

    record = address_book.data[name]

    record.add_birthday(birthday)
    return f"Birthday for {name} added."


@input_error
@contact_exists
def remove_birthday(args, address_book):
    if len(args) != 1:
        raise exceptions.InvalidArgsError

    name = args[0]

    record = address_book.data[name]

    if record.birthday and record.birthday.value:
        record.birthday.value = None
        return f"Birthday removed from {name}."
    else:
        raise exceptions.BirthdayDoesNotExist


@input_error
@contact_exists
def show_birthday(args, address_book):
    if len(args) != 1:
        raise exceptions.InvalidArgsError
    name = args[0]

    record = address_book.data[name]

    if record.birthday.value:
        return f"{name}'s birthday: {record.birthday.value}"


@input_error
def find_contact(args, address_book):
    if len(args) != 1:
        raise exceptions.InvalidArgsError
    symbols = args[0]

    if len(symbols) < 2:
        raise exceptions.InvalidSearchPatternError

    result = address_book.find_record(symbols)
    return result if result else "Nothing was found for the specified string."


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
