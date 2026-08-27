def welcome_message(name):
    return f"{name}, welcome to the Data Engineering course."


def personalized_welcome(name):
    cleaned_name = name.strip()

    if not cleaned_name:
        return "Welcome to the Data Engineering course."

    return welcome_message(cleaned_name)


if __name__ == "__main__":
    name = input("Enter your name: ")
    print(personalized_welcome(name))
