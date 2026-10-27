weight = float(input("Weight (kg): "))
height = float(input("Height (cm): "))

height_m = height / 100
bmi = weight / (height_m ** 2)

print("BMI:", round(bmi, 1))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")