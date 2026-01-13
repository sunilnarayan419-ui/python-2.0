# Hangman in Python

import random

words = ("apple","orange","banana","coconut","pineapple")   


hangman_art = {0:("    ",
                  "    ",
                  "    "),
               1:("  o  ",
                  "    ",
                  "    "),
               2:("  o  ",
                  "  |  ",
                  "    "),
               3:("  o  ",
                  "  /|  ",
                  "    "),
               4:("  o  ",
                  "  /|\\ ",
                  "    "),
               5:("  o  ",
                  "   /|\\ ",
                  "   / "),
               6:("  o  ",
                  " /|\\   ",
                  " /\\   "),}

def display_man(wrong_guesses):
    print(F"**************")
    for line in hangman_art[wrong_guesses]:
        print(line)
        print(F"**************")
        
def displAy_hint(hint):
    print(F"**************")
    print(" ".join(hint))
    print(F"**************")    
    
def display_answer(answer):
    print(F"**************")
    print(" ".join(answer))
    print(F"**************")
    
def mAin():
    answer = random.choice(words)
    hint = ["_"]*len(answer)    
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)  
        guess = input(f"Enter a letter : ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print(f"Invalid input")
            continue
        
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
        
        guessed_letters.add(guess)
        
        if guess in answer :
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess 
        else: 
            wrong_guesses += 1  
            
        if "_ " not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False  
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            is_running = False

if __name__ == " __main__":
    mAin()  
    
    
# SAME PROGRAM BY AI 
import random
from typing import List, Set

# =======================
# CONSTANTS
# =======================

WORDS: tuple[str, ...] = (
    "apple",
    "orange",
    "banana",
    "coconut",
    "pineapple"
)

HANGMAN_ART: dict[int, tuple[str, ...]] = {
    0: (
        "     ",
        "     ",
        "     "
    ),
    1: (
        "  O  ",
        "     ",
        "     "
    ),
    2: (
        "  O  ",
        "  |  ",
        "     "
    ),
    3: (
        "  O  ",
        " /|  ",
        "     "
    ),
    4: (
        "  O  ",
        " /|\\ ",
        "     "
    ),
    5: (
        "  O  ",
        " /|\\ ",
        " /   "
    ),
    6: (
        "  O  ",
        " /|\\ ",
        " / \\ "
    )
}

MAX_WRONG_GUESSES = len(HANGMAN_ART) - 1
SEPARATOR = "=" * 20


# =======================
# DISPLAY FUNCTIONS
# =======================

def display_hangman(wrong_guesses: int) -> None:
    print(SEPARATOR)
    for line in HANGMAN_ART[wrong_guesses]:
        print(line)
    print(SEPARATOR)


def display_hint(hint: List[str]) -> None:
    print("Word:", " ".join(hint))


def display_guessed_letters(guessed_letters: Set[str]) -> None:
    print("Guessed letters:", " ".join(sorted(guessed_letters)))


# =======================
# INPUT VALIDATION
# =======================

def get_valid_guess(guessed_letters: Set[str]) -> str:
    while True:
        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("❌ Letter already guessed.")
            continue

        return guess


# =======================
# GAME LOGIC
# =======================

def update_hint(answer: str, hint: List[str], guess: str) -> bool:
    """Updates hint and returns True if guess was correct"""
    is_correct = False

    for index, letter in enumerate(answer):
        if letter == guess:
            hint[index] = guess
            is_correct = True

    return is_correct


def is_game_won(hint: List[str]) -> bool:
    return "_" not in hint


# =======================
# MAIN GAME LOOP
# =======================

def play_hangman() -> None:
    answer: str = random.choice(WORDS)
    hint: List[str] = ["_"] * len(answer)
    guessed_letters: Set[str] = set()
    wrong_guesses: int = 0

    print("\n🎮 Welcome to Hangman!\n")

    while True:
        display_hangman(wrong_guesses)
        display_hint(hint)
        display_guessed_letters(guessed_letters)

        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if update_hint(answer, hint, guess):
            print("✅ Correct guess!")
        else:
            wrong_guesses += 1
            print("❌ Wrong guess!")

        if is_game_won(hint):
            display_hangman(wrong_guesses)
            print(f"\n🎉 YOU WIN! The word was '{answer}'.")
            break

        if wrong_guesses >= MAX_WRONG_GUESSES:
            display_hangman(wrong_guesses)
            print(f"\n💀 YOU LOSE! The word was '{answer}'.")
            break


# =======================
# ENTRY POINT
# =======================

def main() -> None:
    play_hangman()


if __name__ == "__main__":
    main()
