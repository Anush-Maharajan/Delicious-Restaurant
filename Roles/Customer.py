# Menu items (represented by a list of dictionaries)

        # Menu should be done using file handling
menu = [
    {'id': 1, 'name': 'Burger', 'price': 5.99},
    {'id': 2, 'name': 'Pizza', 'price': 7.99},
    {'id': 3, 'name': 'Pasta', 'price': 6.49},
    {'id': 4, 'name': 'Salad', 'price': 3.99}
]

# Customers (represented by a dictionary)
customers = {} # Need to use file handling

# Orders (represented by a list of dictionaries)
orders = [] # Needs file handling

# Function to display the menu
def show_menu():
    print("Menu:")
    for item in menu:
        print(f"{item['id']}. {item['name']} - ${item['price']}")

# Function to register a customer
def register_customer(name, email, phone):
    customer_id = len(customers) + 1
    customers[customer_id] = {'name': name, 'email': email, 'phone': phone}
    return customer_id

# Function to update customer profile
        
        #No need to do update profile

def update_profile(customer_id, name=None, email=None, phone=None):
    if customer_id in customers:
        if name:
            customers[customer_id]['name'] = name
        if email:
            customers[customer_id]['email'] = email
        if phone:
            customers[customer_id]['phone'] = phone
        print("Profile updated successfully.")
    else:
        print("Customer not found.")

# Function to place an order
def place_order(customer_id, order_items):
    total_price = sum([item['price'] for item in order_items])
    order_id = len(orders) + 1
    order = {
        'order_id': order_id,
        'customer_id': customer_id,
        'items': order_items,
        'total_price': total_price,
        'status': 'Pending'
    }
    orders.append(order)
    return order_id

# Function to view order status
def view_order(order_id):
    for order in orders:
        if order['order_id'] == order_id:
            print(f"Order ID: {order['order_id']}")
            print("Items:")
            for item in order['items']:
                print(f"- {item['name']}")
            print(f"Total Price: ${order['total_price']}")
            print(f"Status: {order['status']}")
            break
    else:
        print("Order not found.")

# Function to update order status
def update_order_status(order_id, status):
    for order in orders:
        if order['order_id'] == order_id:
            order['status'] = status
            print(f"Order {order_id} status updated to {status}.")
            break
    else:
        print("Order not found.")

# Function to send feedback
def send_feedback(customer_id, feedback):
    if customer_id in customers:
        customer_name = customers[customer_id]['name']
        print(f"Feedback from {customer_name}: {feedback}")
    else:
        print("Customer not found.")

# Function to delete an item from an order
def delete_item_from_order(order_id, item_id):
    for order in orders:
        if order['order_id'] == order_id:
            order['items'] = [item for item in order['items'] if item['id'] != item_id]
            order['total_price'] = sum([item['price'] for item in order['items']])
            print(f"Item {item_id} removed from Order {order_id}.")
            break
    else:
        print("Order not found.")

# Main function to simulate the system
def main():
    # Register a customer
    customer_id = register_customer("John Doe", "john@example.com", "1234567890")

    # Display menu and place an order
    show_menu()
    order_items = [menu[0], menu[2]]  # Burger and Pasta
    order_id = place_order(customer_id, order_items)

    # View order status
    print("\nOrder Placed:")
    view_order(order_id)

    # Update order status
    update_order_status(order_id, "Cooking")

    # Customer updates their profile
    update_profile(customer_id, name="John Smith", email="john.smith@example.com")
    print("\nUpdated Profile:")
    print(customers[customer_id])

    # Send feedback
    send_feedback(customer_id, "The food was delicious!")

    # Customer deletes an item from the order
    print("\nDeleting an Item from Order:")
    delete_item_from_order(order_id, 3)  # Removing Pasta

    # View updated order status
    print("\nUpdated Order:")
    view_order(order_id)
