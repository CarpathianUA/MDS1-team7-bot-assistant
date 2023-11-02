import modules.bot_assistant.models.exceptions as exceptions


def input_error(func):
    """
    Decorator for input errors.
    :param func:
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except exceptions.InvalidArgsError:
            return "Invalid number of arguments. Type 'help' to see available commands and their usage."
        except exceptions.ContactAlreadyExistsError:
            return "Contact already exists."
        except exceptions.ContactDoesNotExistError:
            return "Contact doesn't exist."
        except exceptions.BirthdayDoesNotExist:
            return "Birthday doesn't exist."
        except exceptions.PhoneDoesNotExistError:
            return "Phone doesn't exist."
        except exceptions.AddressDoesNotExistError:
            return "Address doesn't exist."
        except exceptions.PhoneAlreadyExistsError:
            return "Phone already exists."
        except exceptions.AddressAlreadyExistsError:
            return "Address already exists."
        except exceptions.InvalidPhoneError:
            return "Invalid phone number. Phone number must contain 10 digits, with or without '+' sign"
        except exceptions.InvalidEmailError:
            return "Invalid email format. Please use john@email.com format"
        except exceptions.EmailAlreadyExistsError:
            return "Email already exists."
        except exceptions.EmailDoesNotExistError:
            return "Email doesn't exist"
        except exceptions.InvalidBirthdayFormatError:
            return "Invalid birthday format. Please use DD.MM.YYYY format."
        except exceptions.InvalidBirthdayRangeError:
            return "The period for showing birthdays is limited to 365 days."
        except exceptions.InvalidSearchPatternError:
            return "Invalid symbols length. Please enter two or more symbols."
        except exceptions.NoteIdAlreadyExisrsError:
            return "Note Id already exists."
        except exceptions.TagDoesNotExistsError:
            return "Tag doesn't exist."
        except exceptions.TagAlreadyExistsError:
            return "Tag already exists."
        except exceptions.NoteAlreadyExistsError:
            return "Note already exists."
        except exceptions.NoteDoesNotExistError:
            return "Note doesn't exist."
        except exceptions.InvalidNoteStatusError:
            return "Invalid status. Status must be 'not_started', 'in_progress', 'completed' or 'postponed'"
        except exceptions.InvalidTextLengthError:
            return "Invalid text length. Text must be maximum 250 symbols."
        except exceptions.InvalidTitleLengthError:
            return "Invalid title length. Title must be maximum 15 symbols."
        except exceptions.InvalidIdValueError:
            return "Invalid Id value. Id must be integer."

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
