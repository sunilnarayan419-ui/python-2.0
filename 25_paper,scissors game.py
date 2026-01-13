import random

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    # Take player input
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"\nPlayer   : {player}")
    print(f"Computer : {computer}")

    # Game logic
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    # Play again option
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != "y":
        running = False

print("\nThanks for playing! 🎮")
