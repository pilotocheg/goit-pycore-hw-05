import phone_book


def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def main():
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        match command:
            case "hello":
                print("How can I help you?")

            case "add":
                print(phone_book.add_contact(args))

            case "change":
                print(phone_book.change_contact(args))

            case "phone":
                print(phone_book.show_phone(args))

            case "all":
                print(phone_book.show_all())

            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
