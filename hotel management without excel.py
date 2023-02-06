class Restaurant:
    def __init__(self, menu):
        self.menu = menu
        self.total = 0
    
    def show_menu(self):
        for item, price in self.menu.items():
            print(f"{item}: ${price}")
    
    def order(self, item, quantity):
        if item in self.menu:
            self.total += self.menu[item] * quantity
            print(f"{quantity} {item} added to cart. Total: ${self.total}")
        else:
            print(f"{item} not available.")
    
    def checkout(self):
        print(f"Total amount payable: ${self.total}")

menu = {
    "Pizza": 15,
    "Burger": 12,
    "Fries": 5,
    "Soda": 3
}

restaurant = Restaurant(menu)

while True:
    print("\nPlease choose an option:")
    print("1. Show Menu")
    print("2. Order")
    print("3. Checkout")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        restaurant.show_menu()
    elif choice == 2:
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        restaurant.order(item, quantity)
    elif choice == 3:
        restaurant.checkout()
        break
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")
