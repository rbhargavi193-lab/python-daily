import random

while True:
    answer = input("Roll dice? (y/n): ")

    if answer == "y":
        roll = random.randint(1, 6)
        print("You rolled:", roll)
    elif answer == "n":
        print("Bye!")
        break
    else:
        print("Type y or n")