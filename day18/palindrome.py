text = input("Word or sentence: ")

reversed_text = text[::-1]
print("Reversed:", reversed_text)

clean = text.lower().replace(" ", "")

if clean == clean[::-1]:
    print("Palindrome!")
else:
    print("Not palindrome")