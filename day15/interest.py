principal = float(input("Money amount: "))
rate = float(input("Rate per year (%): "))
years = float(input("Years: "))

interest = principal * rate * years / 100
total = principal + interest

print("Interest:", interest)
print("Total:", total)