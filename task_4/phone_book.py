from decorators import input_error, phone_validation

contacts = {}


@input_error
@phone_validation
def add_contact(args: list[str]):
    name, phone = args

    if name in contacts:
        return "Contact already exists"

    contacts[name] = phone

    return "Contact added."


@input_error
@phone_validation
def change_contact(args: list[str]):
    name, phone = args

    if contacts[name]:
        contacts[name] = phone

    return "Contact changed."


@input_error
def show_phone(args: list[str]):
    (name,) = args
    return contacts[name]


def show_all():
    return "\n".join([f"{name} {phone}" for name, phone in contacts.items()])
