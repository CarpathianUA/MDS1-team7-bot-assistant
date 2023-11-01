class InvalidArgsError(ValueError):
    pass


class ContactDoesNotExistError(ValueError):
    pass


class ContactAlreadyExistsError(ValueError):
    pass


class PhoneDoesNotExistError(ValueError):
    pass


class PhoneAlreadyExistsError(ValueError):
    pass


class InvalidPhoneError(ValueError):
    pass


class InvalidEmailFormatError(ValueError):
    pass


class InvalidEmailError(ValueError):
    pass


class EmailDoesNotExistError(ValueError):
    pass


class InvalidBirthdayFormatError(ValueError):
    pass


class InvalidBirthdayRangeError(ValueError):
    pass


class BirthdayDoesNotExist(ValueError):
    pass


class InvalidSearchPatternError(ValueError):
    pass


class InvalidTitleLengthError(ValueError):
    pass

class InvalidTextLengthError(ValueError):
    pass


class InvalidNoteStatusError(ValueError):
    pass


class TitleDoesNotExistError(ValueError):
    pass


class NoteAlreadyExistsError(ValueError):
    pass


class TagAlreadyExistsError(ValueError):
    pass