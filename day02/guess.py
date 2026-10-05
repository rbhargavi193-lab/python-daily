import random

secret = random.randint(1, 10)

for attempt in range(3):
    guess = int(input("Guess 1-10: "))
    if guess == secret:
        print("Correct!")
        break
    elif guess > secret:
        print("Too high")
    else:
        print("Too low")
else:
    print("Out of tries, number was", secret)
