import time

seconds = int(input("Seconds to count: "))

while seconds > 0:
    print(seconds)
    time.sleep(1)
    seconds = seconds - 1

print("Time up!")