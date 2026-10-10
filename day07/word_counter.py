filename = input("File name (e.g. sample.txt): ")

try:
    with open("day07/" + filename) as f:
        text = f.read()
except FileNotFoundError:
    print("File not found in day07 folder")
    raise SystemExit

ignore = ["and", "is", "me"]

words = text.lower().split()
useful = []
for word in words:
    if word not in ignore:
        useful.append(word)

print("Lines:", len(text.splitlines()))
print("Words:", len(words))
print("Words after ignoring:", len(useful))
print("Characters:", len(text))

counts = {}
for word in useful:
    counts[word] = counts.get(word, 0) + 1

top = sorted(counts.items(), key=lambda item: item[1], reverse=True)

print("Top 3 words:")
for word, count in top[:3]:
    print(word, count)