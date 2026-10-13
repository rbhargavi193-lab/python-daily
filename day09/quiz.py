import random

questions = [
    {"question": "Which keyword defines a function in Python?", "answer": "def"},
    {"question": "What does len([1, 2, 3]) return?", "answer": "3"},
    {"question": "Which symbol starts a comment in Python?", "answer": "#"},
    {"question": "What is the type of 3.14?", "answer": "float"},
    {"question": "Which function reads user input?", "answer": "input"},
]

random.shuffle(questions)
score = 0

for number, q in enumerate(questions, 1):
    user = input(str(number) + ". " + q["question"] + " ")
    if user.strip().lower() == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong, answer is", q["answer"])

percent = score / len(questions) * 100
print("\nScore:", score, "/", len(questions), "-", percent, "%")

if percent == 100:
    print("Perfect!")
elif percent >= 60:
    print("Good job")
else:
    print("Keep practicing")