# =================================
# Industry Level Biology Quiz Game
# =================================

# Each question is a tuple (question, options, correct_answer)
quiz_questions = [
    ("Which organelle is called the powerhouse of the cell?",
     ("A. Nucleus", "B. Ribosome", "C. Mitochondria", "D. Golgi body"), "C"),

    ("What is the basic unit of life?",
     ("A. Tissue", "B. Cell", "C. Organ", "D. Atom"), "B"),

    ("Which blood group is known as the universal donor?",
     ("A. A", "B. B", "C. AB", "D. O"), "D"),

    ("Photosynthesis occurs in which part of the plant?",
     ("A. Root", "B. Stem", "C. Leaf", "D. Flower"), "C"),

    ("Which vitamin is produced in the human skin?",
     ("A. Vitamin A", "B. Vitamin B", "C. Vitamin C", "D. Vitamin D"), "D"),

    ("What is the genetic material in humans?",
     ("A. RNA", "B. Protein", "C. DNA", "D. Lipid"), "C"),

    ("Which gas is released during photosynthesis?",
     ("A. Oxygen", "B. Carbon dioxide", "C. Nitrogen", "D. Hydrogen"), "A"),

    ("Which part of the brain controls balance?",
     ("A. Cerebrum", "B. Cerebellum", "C. Medulla", "D. Hypothalamus"), "B"),

    ("What is the normal human body temperature?",
     ("A. 35°C", "B. 36°C", "C. 37°C", "D. 38°C"), "C"),

    ("Which organ filters blood in the human body?",
     ("A. Heart", "B. Liver", "C. Kidney", "D. Lungs"), "C")
]

score = 0

print("\n🧠 WELCOME TO THE BIOLOGY QUIZ 🧬")
print("Each question carries 1 mark")
print("--------------------------------\n")

# Quiz Loop (Nested structure)
for index, question in enumerate(quiz_questions, start=1):
    print(f"Q{index}. {question[0]}")

    for option in question[1]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == question[2]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is {question[2]}\n")

# ================================
# Result Section
# ================================
print("=========== RESULT ===========")
print(f"Your Score: {score} / {len(quiz_questions)}")

percentage = (score / len(quiz_questions)) * 100
print(f"Percentage: {percentage:.2f}%")

# Congratulations logic
if score == len(quiz_questions):
    print("\n🏆 CONGRATULATIONS! YOU ARE THE WINNER 🏆")
elif score >= 7:
    print("\n🎉 Excellent Performance! Well Done!")
elif score >= 4:
    print("\n👍 Good Effort! Keep Practicing!")
else:
    print("\n📘 Needs Improvement. Try Again!")

print("\nThank you for playing the Biology Quiz 🧬")
