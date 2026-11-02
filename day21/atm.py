balance = 1000

while True:
    print("\n1 balance | 2 deposit | 3 withdraw | 4 quit")
    choice = input("> ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amount = float(input("Deposit amount: "))
        if amount > 0:
            balance = balance + amount
            print("Done. Balance:", balance)
        else:
            print("Amount must be above 0.")

    elif choice == "3":
        amount = float(input("Withdraw amount: "))
        if amount <= 0:
            print("Amount must be above 0.")
        elif amount > balance:
            print("Not enough money.")
        else:
            balance = balance - amount
            print("Done. Balance:", balance)

    elif choice == "4":
        print("Bye!")
        break

    else:
        print("Pick 1-4.")