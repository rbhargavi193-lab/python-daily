import random
import string

length = int(input("Password length: "))

if length < 8:
    print("Too short")
else:
    use_symbols = input("Include symbols? (y/n): ").lower()

    chars = string.ascii_letters + string.digits
    if use_symbols == "y":
        chars += string.punctuation

    count = int(input("How many passwords: "))

    for n in range(count):
        password = ""
        for i in range(length):
            password += random.choice(chars)
        print(n + 1, password)