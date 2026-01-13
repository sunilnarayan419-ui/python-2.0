import random

low = 1
high = 100 
options = ("rock","paper","scissors")
card = ["2","3","4","5","6","7","8","9","10","11","J","k"]

print(help(random)) 

number = random.randint(low, high )
number = random.random() 
options = random.choice(options)
print(random.shuffle(card))


print(number)

# ex 1
# Python number guessing game
import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num) 
guesses = 0
is_running = True

print("Python Number Guessing game")
print("Select a number between {lowest_num} and {highest}") 

while is_running:
    guess = input("Enter your guess : ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < lowest_num or guess > highest_num:
            print(f"That number is out of range")
            print("Please Select a number between {lowest_num} and {highest}")
        elif guess < answer:
            print("Too low Try again")
        elif guess > answer:
            print("Too high Try again!")
        else: 
            print(f"CORRECT ! The answer was : {answer}")
            print(f"Number of guesses : {guesses}")
            is_running = False
            
    else: 
        print("Invalid guess") 
        print("Please Select a number between {lowest_num} and {highest}")
    
    # same program by AI
    # =====================================
# Industry-Level Number Guessing Game
# =====================================

import random


def play_game():
    LOWEST_NUM = 1
    HIGHEST_NUM = 100

    answer = random.randint(LOWEST_NUM, HIGHEST_NUM)
    attempts = 0

    print("\n🎯 Welcome to the Number Guessing Game")
    print(f"Guess a number between {LOWEST_NUM} and {HIGHEST_NUM}\n")

    while True:
        user_input = input("Enter your guess: ")

        if not user_input.isdigit():
            print("❌ Invalid input. Please enter a valid number.\n")
            continue

        guess = int(user_input)
        attempts += 1

        if guess < LOWEST_NUM or guess > HIGHEST_NUM:
            print(f"⚠️  Out of range. Choose between {LOWEST_NUM} and {HIGHEST_NUM}.\n")
        elif guess < answer:
            print("⬇️  Too low. Try again.\n")
        elif guess > answer:
            print("⬆️  Too high. Try again.\n")
        else:
            print("🎉 Congratulations! You guessed the correct number.")
            print(f"✅ Answer        : {answer}")
            print(f"🔢 Attempts used : {attempts}")
            break


def main():
    play_game()


if __name__ == "__main__":
    main()
