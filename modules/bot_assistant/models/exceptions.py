class ContactDoesNotExistError(ValueError):
    pass


class ContactAlreadyExistsError(ValueError):
    pass


class PhoneDoesNotExistError(ValueError):
    pass


class InvalidPhoneError(ValueError):
    pass


class InvalidBirthdayFormatError(ValueError):
    pass


class InvalidArgsError(ValueError):
    pass


class InvalidBirthdayRangeError(ValueError):
    pass


class InvalidSearchPatternError(ValueError):
    pass
