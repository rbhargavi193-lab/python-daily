tasks = []

while True:
    print("\n1. Add  2. Show  3. Done  4. Quit")
    choice = input("Choose: ")

    if choice == "1":
        task = input("Task: ")
        tasks.append(task)
    elif choice == "2":
        for i, task in enumerate(tasks, 1):
            print(i, task)
    elif choice == "3":
        num = int(input("Number done: "))
        tasks.pop(num - 1)
    elif choice == "4":
        break
    else:
        print("Invalid")