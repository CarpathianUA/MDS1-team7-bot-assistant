import modules.bot_assistant.models.exceptions as exceptions
from modules.bot_assistant.models.exceptions import InvalidIdValueError


# Mapping of exceptions to their corresponding error messages
exception_to_message = {
    exceptions.InvalidArgsError: (
        "Invalid number of arguments. Type 'help' to see available commands "
        "and their usage."
    ),
    exceptions.ContactAlreadyExistsError: "Contact already exists.",
    exceptions.ContactDoesNotExistError: "Contact doesn't exist.",
    exceptions.BirthdayDoesNotExist: "Birthday doesn't exist.",
    exceptions.PhoneDoesNotExistError: "Phone doesn't exist.",
    exceptions.AddressDoesNotExistError: "Address doesn't exist.",
    exceptions.PhoneAlreadyExistsError: "Phone already exists.",
    exceptions.AddressAlreadyExistsError: "Address already exists.",
    exceptions.InvalidPhoneError: (
        "Invalid phone number. Phone number must contain from 10 to 12 digits, with or "
        "without '+' sign."
    ),
    exceptions.InvalidEmailError: (
        "Invalid email format. Please use alan@wake.com format."
    ),
    exceptions.EmailAlreadyExistsError: "Email already exists.",
    exceptions.EmailDoesNotExistError: "Email doesn't exist",
    exceptions.InvalidBirthdayFormatError: (
        "Invalid birthday format. Please use DD.MM.YYYY format."
    ),
    exceptions.InvalidBirthdayRangeError: (
        "The period for showing birthdays is limited to 365 days."
    ),
    exceptions.InvalidSearchPatternError: (
        "Invalid symbols length. Please enter two or more symbols."
    ),
    exceptions.NoteIdAlreadyExisrsError: "Note Id already exists.",
    exceptions.TagDoesNotExistsError: "Tag doesn't exist.",
    exceptions.TagAlreadyExistsError: "Tag already exists.",
    exceptions.NoteAlreadyExistsError: "Note already exists.",
    exceptions.NoteDoesNotExistError: "Note doesn't exist.",
    exceptions.InvalidNoteStatusError: (
        "Invalid status. Status must be 'not_started', 'in_progress', "
        "'completed' or 'postponed'."
    ),
    exceptions.InvalidTextLengthError: (
        "Invalid text length. Text must be maximum 250 symbols."
    ),
    exceptions.InvalidTitleLengthError: (
        "Invalid title length. Title must be maximum 15 symbols."
    ),
    exceptions.InvalidIdValueError: "Invalid Id value. Id must be integer.",
    exceptions.InvalidTagLengthError: "Invalid tag length. Tag must be maximum 10 symbols.",
}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        # We inherit custom exceptions from ValueError
        # which inherits from Exception base class
        # pylint: disable=E0712
        except tuple(exception_to_message) as e:
            return exception_to_message[type(e)]

    return wrapper


def contact_exists(func):
    def wrapper(args, address_book):
        if len(args) < 1:
            raise exceptions.InvalidArgsError

        name = args[0]
        if name not in address_book.data:
            raise exceptions.ContactDoesNotExistError

        return func(args, address_book)

    return wrapper


def validate_id(func):
    def wrapper(args, notes):
        try:
            if any(args):
                int(args[0])
            else:
                raise exceptions.InvalidArgsError

        except ValueError as e:
            raise InvalidIdValueError from e

        return func(args, notes)

    return wrapper
