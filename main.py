import random
import string
from settings import settings

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
all_symbols = lowercase + uppercase + numbers + symbols

# Use characters only once?
if settings["use_doubles"]:
    # Randomize letters and add to array with doubles
    password_array = [random.choice(all_symbols)
                      for i in range(settings["length"])]
else:
    try:
        # Randomise letters and add to array with no doubles
        password_array = random.sample(all_symbols, settings["length"])
    except:
        # Not enough characters to fill array length
        password_array = f"Password too long: turn off \"only_unique\" if you want a password this long, or change " \
                         f"password length to something lower or equal to {len(all_symbols)} "

# Make array to string
password = "".join(password_array)

# Print password
print(f"\nGenerated Password:\n\033[92m{password}\033[0m\n")

# TODO Main function
