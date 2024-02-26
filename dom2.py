def main():
    contacts = {}

    def parse_input(user_input):
        cmd, *args = user_input.split()
        return cmd.lower(), args

    def add_contact(args, contacts):
        if len(args) != 2:
            return "Будь ласка, вкажіть ім'я та номер телефону."
        name, phone = args
        contacts[name] = phone
        return "Контакт додано."

    def change_contact(args, contacts):
        if len(args) != 2:
            return "Вкажіть ім'я та новий номер телефону."
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Контакт оновлено."
        else:
            return "Контакт не знайдено."

    def show_phone(args, contacts):
        if len(args) != 1:
            return "Вкажіть назву."
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Контакт не знайдено."

    def show_all(contacts):
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()]) if contacts else "Контакти не знайдено."

    print("Ласкаво просимо до бота-помічника!")
    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("Чим я можу вам допомогти?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


