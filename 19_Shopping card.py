foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else: 
        price = float(input("Enter the price of a {food} : $ ")) 
        foods.append(food)
        prices.append(price)
        
print("-----YOUR ORDER-----")

for food in foods :
    print(food, end= " ")
    
for price in prices:
    total +=  price 

print()    
print(f"Your total is : ${total}")
print("------THANK YOU SIR------")

# shopping card by AI
# ================================
# Industry-Level Shopping Cart
# ================================

# Product catalog (tuple: id, name, price, category)
products = (
    (1, "Laptop", 55000, "Electronics"),
    (2, "Smartphone", 25000, "Electronics"),
    (3, "Headphones", 2000, "Accessories"),
    (4, "Book", 500, "Education"),
    (5, "Pen", 50, "Stationery"),
)

# Extract unique categories using set
categories = set()
for p in products:
    categories.add(p[3])

cart = []   # list to store cart items (id, name, price, qty)

# ================================
# Display Products
# ================================
def show_products():
    print("\n--- Available Products ---")
    for pid, name, price, category in products:
        print(f"{pid}. {name} | ₹{price} | {category}")

# ================================
# Add to Cart
# ================================
def add_to_cart():
    show_products()
    pid = int(input("\nEnter Product ID to add: "))
    qty = int(input("Enter Quantity: "))

    for product in products:
        if product[0] == pid:
            cart.append((product[0], product[1], product[2], qty))
            print(f"✅ {product[1]} added to cart")
            return
    print("❌ Invalid Product ID")

# ================================
# View Cart
# ================================
def view_cart():
    if not cart:
        print("\n🛒 Cart is empty")
        return

    print("\n--- Your Cart ---")
    total = 0

    for pid, name, price, qty in cart:
        cost = price * qty
        total += cost
        print(f"{name} | ₹{price} x {qty} = ₹{cost}")

    print(f"💰 Total Amount: ₹{total}")

# ================================
# Checkout
# ================================
def checkout():
    if not cart:
        print("\n❌ Cart is empty")
        return

    view_cart()
    print("\n✅ Checkout successful. Thank you for shopping!")
    cart.clear()

# ================================
# Main Menu (Nested Loop)
# ================================
while True:
    print("\n========== SHOP MENU ==========")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_products()

    elif choice == "2":
        add_to_cart()

    elif choice == "3":
        view_cart()

    elif choice == "4":
        checkout()

    elif choice == "5":
        print("\n👋 Thank you! Visit again.")
        break

    else:
        print("❌ Invalid choice, try again")

