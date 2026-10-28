name = input("Student name: ")

maths = float(input("Maths marks (0-100): "))
science = float(input("Science marks (0-100): "))
english = float(input("English marks (0-100): "))

total = maths + science + english
average = total / 3

print("\nName:", name)
print("Total:", total)
print("Average:", round(average, 1))

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 40:
    print("Grade: D")
else:
    print("Grade: F")