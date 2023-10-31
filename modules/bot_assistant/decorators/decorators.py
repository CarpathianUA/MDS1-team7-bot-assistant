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
        except exceptions.PhoneDoesNotExistError:
            return "Phone doesn't exist."
        except exceptions.InvalidPhoneError:
            return "Invalid phone number. Phone number must contain 10 digits, with or without '+' sign"
        except exceptions.InvalidEmailError:
            return "Invalid email format. Please use john@email.com format"
        except exceptions.EmailDoesNotExistError:
            return "Email doesn`t exist"
        except exceptions.ContactWithThisBirthdayDoesNotExist:
            return "Invalid birthday format. Please use DD.MM.YYYY format."
        except exceptions.InvalidBirthdayFormatError:
            return "Invalid birthday format. Please use DD.MM.YYYY format."

    return wrapper
