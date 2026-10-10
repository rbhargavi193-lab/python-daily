def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

history = []

while True:
    print("\n1. Add  2. Subtract  3. Multiply  4. Divide  5. Power  6. History  7. Quit")
    choice = input("Choose: ")

    if choice == "7":
        break

    if choice == "6":
        if not history:
            print("No history yet")
        for item in history:
            print(item)
        continue

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice")
        continue

    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
    except ValueError:
        print("Enter numbers only")
        continue

    if choice == "1":
        result = add(a, b)
        symbol = "+"
    elif choice == "2":
        result = subtract(a, b)
        symbol = "-"
    elif choice == "3":
        result = multiply(a, b)
        symbol = "*"
    elif choice == "4":
        result = divide(a, b)
        symbol = "/"
    else:
        result = power(a, b)
        symbol = "**"

    print("Result:", result)
    history.append(str(a) + " " + symbol + " " + str(b) + " = " + str(result))