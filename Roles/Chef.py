import UTILs.enhancer as enhancer

order = []
ingredient = []
user_profile = []

#View order placed by customer
def view_order():
    return order

#Update orders as "In Progress" or "Completed.” 
def update_order_status(order_id, new_status): 
    if order_id in order:
        order[order_id]["status"] = new_status
        print(f"Order {order_id} is now {new_status}")
    else:
        print(f"Order {order_id} not found")
    
# Add Ingredient
def add_ingredient(ingredient_id, name, quantity):
    ingredient[ingredient_id] = {"name": name, "quantity": quantity}
    print(f"Added ingredient: {name} with ID {ingredient_id}")  

#Edit Ingredient
def edit_ingredient(ingredient_id, name, quantity): 
    if ingredient_id in ingredient:
        ingredient[ingredient_id] = {"name": name, "quantity": quantity}
        print(f"Edited ingredient ID {ingredient_id} to: {name}, quantity: {quantity}")
    else:
        print(f"Ingredient ID {ingredient_id} not found")

#Delete Ingredient
def delete_ingredient(ingredient_id):
    if ingredient_id in ingredient:
        del ingredient[ingredient_id]
        print(f"Deleted ingredient ID {ingredient_id}")
    else:
        print(f"Ingredient ID {ingredient_id} not found")

def home_layer(receivedData):
    enhancer.waitingFunction()
    print(f"Welcome {receivedData[1]}! What would you like to do?\n")
    print("1. View Order.")
