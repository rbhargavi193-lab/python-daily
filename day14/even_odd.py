while True:
    text = input("Number (q to quit): ")

    if text == "q":
        print("Bye!")
        break

    number = int(text)

    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")