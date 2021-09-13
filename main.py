import random
import string
from settings import settings


def get_symbols():
    # Use lowercase, uppercase and numbers?
    lowercase = string.ascii_lowercase if settings["use_lowercase"] else ""
    uppercase = string.ascii_uppercase if settings["use_lowercase"] else ""
    numbers = string.digits if settings["use_numbers"] else ""

    # Use symbols, custom symbols or no symbols?
    if settings["custom_symbols"]:
        symbols = settings["custom_symbols"]
    else:
        symbols = string.punctuation if settings["use_symbols"] else ""

    # Add all symbols to one string
    return lowercase + uppercase + numbers + symbols


def generate_password(custom_length):
    # Use custom length?
    if custom_length.isdigit():
        if int(custom_length) > -1:
            custom_length = int(custom_length)
        else:
            print("Lengh must be positive")
    else:
        print("Length is not a int value")

    if custom_length == 0:
        length = settings["length"]
    elif custom_length > 0:
        length = int(custom_length)

    # Use characters only once?
    if settings["use_doubles"]:
        # Randomize letters and add to array with doubles
        password_array = [random.choice(get_symbols())
                          for i in range(length)]
    else:
        try:
            # Randomise letters and add to array with no doubles
            password_array = random.sample(get_symbols(), length)
        except:
            # Not enough characters to fill array length
            password_array = f"\n\033[91mPassword too long: turn off \"only_unique\" if you want a password this long, or change " \
                f"password length to something lower or equal to {len(get_symbols())}\033[0m"
    return "".join(password_array)


if __name__ == "__main__":
    active = True
    print("\n\033[96m### Minimal Python Password Generator ###\033[0m")
    while active:
        command = input(
            "\nHow many characters should the password have? Type 0 for default value in settings.py, type exit to quit.\n-> ")
        if command.lower() == "exit":
            print(f"\n\033[91mExiting...\033[0m\n")
            active = False
        elif command.lower() == "settings":
            print(settings)
        elif command.isdigit():
            print(
                f"\nGenerated Password:\n\033[92m{generate_password(command)}\033[0m\n")
        else:
            print(f"\n\033[91mTyping mistake!\033[0m\n")
