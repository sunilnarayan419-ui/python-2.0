# Python Slot Machine
import random

SYMBOLS = ['❤️', '💕', '😍', '😘']


def spin_row():
    """Randomly selects 3 symbols for a slot spin"""
    return [random.choice(SYMBOLS) for _ in range(3)]


def print_row(row):
    """Displays the slot row"""
    print("**********************")
    print(" | ".join(row))
    print("**********************")


def get_payout(row, bet):
    """Calculates payout based on matching symbols"""
    if row[0] == row[1] == row[2]:
        if row[0] == '❤️':
            return bet * 3
        elif row[0] == '💕':
            return bet * 4
        elif row[0] == '😍':
            return bet * 5
        elif row[0] == '😘':
            return bet * 6
    return 0


def main():
    balance = 100

    print("**********************")
    print(" Welcome to Python Slot ")
    print(" Symbols:", " ".join(SYMBOLS))
    print("**********************")

    while balance > 0:
        print(f"\nCurrent Balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("❌ Please enter a valid number")
            continue

        bet = int(bet)

        if bet <= 0:
            print("❌ Bet must be greater than 0")
            continue

        if bet > balance:
            print("❌ Insufficient funds")
            continue

        balance -= bet

        print("\nSpinning...\n")
        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"🎉 You won ${payout}!")
        else:
            print("😢 You lost this round")

        balance += payout

        play_again = input("\nPlay again? (Y/N): ").upper()
        if play_again != 'Y':
            break

    print("\n*********************************************")
    print(f"Game Over! Final Balance: ${balance}")
    print("*********************************************")


if __name__ == "__main__":
    main()
