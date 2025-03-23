import UTILs.enhancer as enhancer
import os

ORDER_FILE = "Database/order.txt"
INGREDIENT_FILE = "Database/ingredients.txt"

def view_order():
    with open(ORDER_FILE, "r") as file:
        orders = file.readlines()
        for order in orders:
            userID, foodItem, status = order.strip().split(";")
            print(f"{userID}\t{foodItem}\t{status}")

def update_order_status(order_id, new_status):
    updated_orders = []
    found = False
    with open(ORDER_FILE, "r") as file:
        orders = file.readlines()
        for order in orders:
            userID, foodItem, status = order.strip().split(";")
            if userID == order_id:
                updated_orders.append(f"{userID};{foodItem};{new_status}\n")
                found = True
            else:
                updated_orders.append(order)
    
    if found:
        with open(ORDER_FILE, "w") as file:
            file.writelines(updated_orders)
        print(f"Order {order_id} updated to {new_status}.")
    
    else:
        print(f"Order {order_id} not found.")

def add_ingredient(ingredient_id, name, quantity):
    with open(INGREDIENT_FILE, "a") as file:
        file.write(f"{ingredient_id};{name};{quantity}\n")
    print(f"Added ingredient: {name} with ID {ingredient_id}.")

def edit_ingredient(ingredient_id, name, quantity):
    updated_ingredients = []
    found = False
    with open(INGREDIENT_FILE, "r") as file:
        ingredients = file.readlines()
        for ingredient in ingredients:
            ing_id, ing_name, ing_quantity = ingredient.strip().split(";")
            if ing_id == ingredient_id:
                updated_ingredients.append(f"{ingredient_id};{name};{quantity}\n")
                found = True
            else:
                updated_ingredients.append(ingredient)
    
    if found:
        with open(INGREDIENT_FILE, "w") as file:
            file.writelines(updated_ingredients)
        print(f"Edited ingredient ID {ingredient_id}.")
    else:
        print(f"Ingredient ID {ingredient_id} not found.")

def delete_ingredient(ingredient_id):
    updated_ingredients = []
    found = False
    with open(INGREDIENT_FILE, "r") as file:
        ingredients = file.readlines()
        for ingredient in ingredients:
            ing_id, _, _ = ingredient.strip().split(";")
            if ing_id == ingredient_id:
                found = True
            else:
                updated_ingredients.append(ingredient)
    
    if found:
        with open(INGREDIENT_FILE, "w") as file:
            file.writelines(updated_ingredients)
        print(f"Deleted ingredient ID {ingredient_id}.")
    else:
        print(f"Ingredient ID {ingredient_id} not found.")

def handle_exit(receivedData):
    os._exit(0)

handleFunctions = {
    "1": view_order,
    "2": update_order_status,
    "3": edit_ingredient,
    "4": delete_ingredient,
    "5": handle_exit
}

def home_layer(receivedData):
    enhancer.waitingFunction()
    while True:
        print(f"Welcome {receivedData[1]}! What would you like to do?\n")
        print("1. View Order.")
        print("2. Add Ingredient.")
        print("3. Edit Ingredient.")
        print("4. Delete Ingredient.")
        print("5. Logout and Exit.")
        userInput = input("Enter the number of the option/n--> ")
        
        if userInput == "2":
            ingredient_id = input("Enter Ingredient ID: ")
            name = input("Enter Ingredient Name: ")
            quantity = input("Enter Ingredient Quantity: ")
            add_ingredient(ingredient_id, name, quantity)
        elif userInput in handleFunctions:
            handleFunctions[userInput]()
        else:
            enhancer.InvalidOption()
