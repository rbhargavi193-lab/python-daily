text = input("Word or sentence: ")

vowels = "aeiou"
count = 0

for letter in text.lower():
    if letter in vowels:
        count = count + 1

print("Vowels:", count)
print("Total characters:", len(text))