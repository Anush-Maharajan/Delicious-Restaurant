def load_menu():
    try:
        with open("Database/menu.txt", "r") as file:
            menu = {}
            for line in file:
                item, price = line.strip().split(";")
                menu[item] = float(price)
            return menu
    except FileNotFoundError:
        return {"Pizza": 12.99, "Burger": 8.99, "Pasta": 10.99}

def save_order(order):
    with open("Database/orders.txt", "a") as file:
        file.write(f"{UserData[0]};{order};PENDING\n")

def view_menu():
    menu = load_menu()
    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item}: ${price}")

def order_food():
    menu = load_menu()
    item_name = input("Enter food item to order: ")
    if item_name in menu:
        save_order(f"{item_name} (In Progress)")
        print(f"{item_name} has been added to your order.")
    else:
        print("Item not found in the menu.")

def view_order_status():
    try:
        with open("orders.txt", "r") as file:
            orders = file.readlines()
            if not orders:
                print("No orders placed yet.")
                return
            print("Your orders:")
            for order in orders:
                print(f"- {order.strip()}")
    except FileNotFoundError:
        print("No orders placed yet.")

def send_feedback():
    feedback = input("Enter your feedback: ")
    with open("feedback.txt", "a") as file:
        file.write(feedback + "\n")
    print("Thank you for your feedback!")

def home_layer(receivedData):
    global UserData; UserData = receivedData
    while True:
        print("\nWelcome to the Restaurant Management System," + receivedData[1])
        print("1. View Menu")
        print("2. Order Food")
        print("3. View Order Status")
        print("4. Send Feedback")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            view_menu()
        elif choice == "2":
            order_food()
        elif choice == "3":
            view_order_status()
        elif choice == "4":
            send_feedback()
        elif choice == "5":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please try again.")