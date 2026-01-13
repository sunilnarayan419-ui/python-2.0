# Concession stand program
# dictionary  {key : value}

menu = {"pizza" : 3.00,
        "nachos": 4.50,
        "popcon":6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print(f"_______MENU________")
for key , value in menu.items():
    print(f"{key:10} : ${value:.2f}")
print(f"_______________")
    
while True:
    food = str(input(f"Select an item (q to quit): ")).lower()  
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print(cart)

for food in cart :
    total =  menu.get(food)
    print(food , end=" ")
    
    print()
    print(f"Total is : ${total:.2f}")
    
# same code by AI
# =====================================
# Industry-Level Concession Stand System
# =====================================

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

cart = []   # stores selected food items


# -------------------------------
# Display Menu
# -------------------------------
def show_menu():
    print("\n========== MENU ==========")
    for item, price in menu.items():
        print(f"{item.capitalize():10} : $ {price:.2f}")
    print("==========================\n")


# -------------------------------
# Add Items to Cart
# -------------------------------
def take_order():
    while True:
        choice = input("Select an item (q to quit): ").lower()

        if choice == "q":
            break
        elif choice in menu:
            cart.append(choice)
            print(f"✅ {choice.capitalize()} added to cart")
        else:
            print("❌ Item not available")


# -------------------------------
# Display Bill
# -------------------------------
def checkout():
    if not cart:
        print("\n🛒 Cart is empty")
        return

    total = 0
    print("\n========== YOUR ORDER ==========")

    for item in cart:
        price = menu[item]
        total += price
        print(f"{item.capitalize():10} : $ {price:.2f}")

    print("--------------------------------")
    print(f"TOTAL AMOUNT      : $ {total:.2f}")
    print("================================")
    print("🙏 Thank you! Visit again.")


# -------------------------------
# Main Program
# -------------------------------
def main():
    print("🍿 Welcome to the Concession Stand 🍕")
    show_menu()
    take_order()
    checkout()


# Run Program
main()
