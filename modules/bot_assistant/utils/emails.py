import re


def validate_email(email):
    """
    Validate email.
    :param email:
    """
    # john@email.com
    pattern = re.compile(r"\b[A-Za-z][A-Za-z0-9._]+@[A-Za-z]+\.[A-Za-z]{2,}\b")
    return bool(pattern.match(email))


def is_valid_email(email):
    """
    Check if email is valid.
    :param email:
    """
    if validate_email(email):
        return email
