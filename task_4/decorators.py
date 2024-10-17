from functools import wraps
import re


def parse_value_error(e: ValueError):
    err_message = str(e)

    match = re.search(
        r"not enough values to unpack \(expected (\d), got (\d)", err_message
    )

    if match:
        expected = int(match.group(1))
        actual = int(match.group(2))
        missing = expected - actual
        return f"Should be {missing} argument{"s" if missing > 1 else ""} after the command"

    return err_message


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return parse_value_error(e)
        except KeyError:
            return "Contact not found"

    return inner


def phone_validation(func):
    @wraps(func)
    def inner(*args, **kwargs):
        _, phone = args[0]

        if not re.match(r"(\+?38)?0\d{9}", phone):
            return "Incorrect phone"

        return func(*args, **kwargs)

    return inner
