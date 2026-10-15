import random

heads = 0
tails = 0

while True:
    answer = input("Flip coin? (y/n): ")

    if answer == "y":
        flip = random.choice(["Heads", "Tails"])
        print("You got:", flip)

        if flip == "Heads":
            heads = heads + 1
        else:
            tails = tails + 1

    elif answer == "n":
        print("Heads:", heads)
        print("Tails:", tails)
        print("Bye!")
        break

    else:
        print("Type y or n")