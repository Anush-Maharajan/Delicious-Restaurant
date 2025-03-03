def manage_customers():
    # Function to manage customers (Add, Edit, Delete).
    while True:
        print("\n=== Manage Customers ===")
        print("1. Add Customer")
        print("2. Edit Customer")
        print("3. Delete Customer")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            edit_customer()
        elif choice == "3":
            delete_customer()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def add_customer():
    # Function to add a new customer.
    print("\n=== Add Customer ===")
    customer_id = input("Enter Customer ID: ")
    name = input("Enter Customer Name: ")
    email = input("Enter Customer Email: ")
    phone = input("Enter Customer Phone: ")

    # Save customer data to a text file (customers.txt)
    with open("customers.txt", "a") as file:
        file.write(f"{customer_id},{name},{email},{phone}\n")
    print("Customer added successfully!")

def edit_customer():
    # Function to edit an existing customer.
    print("\n=== Edit Customer ===")
    customer_id = input("Enter Customer ID to edit: ")
    customers = []

    # Load existing customers from the file
    try:
        with open("customers.txt", "r") as file:
            for line in file:
                customers.append(line.strip().split(","))
    except FileNotFoundError:
        print("No customers found.")
        return

    # Find the customer to edit
    found = False
    for i, customer in enumerate(customers):
        if customer[0] == customer_id:
            found = True
            print(f"Editing Customer: {customer}")
            name = input("Enter new Name: ")
            email = input("Enter new Email: ")
            phone = input("Enter new Phone: ")
            customers[i] = [customer_id, name, email, phone]
            break

    if not found:
        print("Customer not found.")
        return

    # Save updated customers back to the file
    with open("customers.txt", "w") as file:
        for customer in customers:
            file.write(",".join(customer) + "\n")
    print("Customer updated successfully!")

def delete_customer():
    # Function to delete a customer.
    print("\n=== Delete Customer ===")
    customer_id = input("Enter Customer ID to delete: ")
    customers = []

    # Load existing customers from the file
    try:
        with open("customers.txt", "r") as file:
            for line in file:
                customers.append(line.strip().split(","))
    except FileNotFoundError:
        print("No customers found.")
        return

    # Find and remove the customer
    found = False
    updated_customers = []
    for customer in customers:
        if customer[0] == customer_id:
            found = True
            print(f"Deleting Customer: {customer}")
        else:
            updated_customers.append(customer)

    if not found:
        print("Customer not found.")
        return

    # Save updated customers back to the file
    with open("customers.txt", "w") as file:
        for customer in updated_customers:
            file.write(",".join(customer) + "\n")
    print("Customer deleted successfully!")

def manage_menu():
    # Function to manage menu categories and pricing.
    while True:
        print("\n=== Manage Menu ===")
        print("1. Add Menu Item")
        print("2. Edit Menu Item")
        print("3. Delete Menu Item")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_menu_item()
        elif choice == "2":
            edit_menu_item()
        elif choice == "3":
            delete_menu_item()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def add_menu_item():
    # Function to add a new menu item.
    print("\n=== Add Menu Item ===")
    item_id = input("Enter Item ID: ")
    name = input("Enter Item Name: ")
    category = input("Enter Item Category: ")
    price = input("Enter Item Price: ")

    # Save menu item to a text file (menu.txt)
    with open("menu.txt", "a") as file:
        file.write(f"{item_id},{name},{category},{price}\n")
    print("Menu item added successfully!")

def edit_menu_item():
    # Function to edit an existing menu item.
    print("\n=== Edit Menu Item ===")
    item_id = input("Enter Item ID to edit: ")
    menu_items = []

    # Load existing menu items from the file
    try:
        with open("menu.txt", "r") as file:
            for line in file:
                menu_items.append(line.strip().split(","))
    except FileNotFoundError:
        print("No menu items found.")
        return

    # Find the menu item to edit
    found = False
    for i, item in enumerate(menu_items):
        if item[0] == item_id:
            found = True
            print(f"Editing Menu Item: {item}")
            name = input("Enter new Name: ")
            category = input("Enter new Category: ")
            price = input("Enter new Price: ")
            menu_items[i] = [item_id, name, category, price]
            break

    if not found:
        print("Menu item not found.")
        return

    # Save updated menu items back to the file
    with open("menu.txt", "w") as file:
        for item in menu_items:
            file.write(",".join(item) + "\n")
    print("Menu item updated successfully!")

def delete_menu_item():
    # Function to delete a menu item.
    print("\n=== Delete Menu Item ===")
    item_id = input("Enter Item ID to delete: ")
    menu_items = []

    # Load existing menu items from the file
    try:
        with open("menu.txt", "r") as file:
            for line in file:
                menu_items.append(line.strip().split(","))
    except FileNotFoundError:
        print("No menu items found.")
        return

    # Find and remove the menu item
    found = False
    updated_menu = []
    for item in menu_items:
        if item[0] == item_id:
            found = True
            print(f"Deleting Menu Item: {item}")
        else:
            updated_menu.append(item)

    if not found:
        print("Menu item not found.")
        return

    # Save updated menu items back to the file
    with open("menu.txt", "w") as file:
        for item in updated_menu:
            file.write(",".join(item) + "\n")
    print("Menu item deleted successfully!")

def view_ingredient_requests():
    # Function to view ingredient requests.
    print("\n=== View Ingredient Requests ===")
    try:
        with open("ingredient_requests.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No ingredient requests found.")

def update_profile():
    # Function to update manager's profile.
    print("\n=== Update Profile ===")
    new_password = input("Enter new password: ")
    # Save updated password to the users.txt file (you can implement this based on your system)
    print("Profile updated successfully!")

def home_layer():
    # Main menu for the Manager.
    while True:
        print("\n=== Manager Dashboard ===")
        print("1. Manage Customers")
        print("2. Manage Menu")
        print("3. View Ingredient Requests")
        print("4. Update Profile")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            manage_customers()
        elif choice == "2":
            manage_menu()
        elif choice == "3":
            view_ingredient_requests()
        elif choice == "4":
            update_profile()
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    home_layer()