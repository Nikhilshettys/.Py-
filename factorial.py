# Python Quiz

questions = (
    "How many elements are in the periodic table?:",
    "Which animal lays the largest eggs?:",
    "What is the most abundant gas in Earth's atmosphere?:",
    "Which planet in the solar system is the hottest?:"
)

options = (
    ("A.116", "B.117", "C.118", "D.119"),
    ("A.Whale", "B.Crocodile", "C.Elephant", "D.Ostrich"),
    ("A.Nitrogen", "B.Oxygen", "C.Carbon Dioxide", "D.Hydrogen"),
    ("A.Mercury", "B.Venus", "C.Earth", "D.Mars")
)

answers = ("C", "D", "A", "B")

guesses = []
score = 0

for question_num in range(len(questions)):
    print("------------------")
    print(questions[question_num])

    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        print("Correct! ✅")
        score += 1
    else:
        print("Incorrect ❌")
        print(f"The correct answer is {answers[question_num]}.")

# Final Score
print("\n------------------")
print(f"Your final score: {score}/{len(questions)}")
print(f"Your percentage: {score / len(questions) * 100:.2f}%")
