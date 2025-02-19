import UTILs.enhancer as enhancer
from UTILs.updateProfile import UpdateProfile
import os

def handle_manage(receivedData):
    print("\nWhat do you want to do?\n")
    print("1. Show all user data.")
    print("2. Edit User Data.")
    print("3. Add User Data.")
    print("4. Delete User Data.")
    userChoice = input("Enter the number --> ")

    if userChoice:
        handle_data[userChoice]()
    else:
        enhancer.InvalidOption()
   
def data_show():
    userData = enhancer.give_User_list()
    print("\nDisplaying all the user data:\n")
    for user in userData:
        print("\t".join(user))

def data_edit():
    pass

def data_add():
    addData = True
    while addData:
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        role = input("Enter Role: ")
        id = enhancer.userID_increment()

        with open("Database/user.txt", "a") as file:
            file.write(f"{id},{name},{email},{password},{role}\n")

        wannaAddData = input("Do you want to add more data?[y/n]\n--> ")
        if wannaAddData.lower() == "y":
            addData = True
        elif wannaAddData.lower() == "n":
            addData = False
        else:
            enhancer.InvalidOption()

def data_delete():
    pass

handle_data = {
    "1": data_show,
    "2": data_edit,
    "3": data_add,
    "4": data_delete
}

def handle_reports(receivedData):

    pass

def handle_feedback(receivedData):
    with open("feedbacks.txt", "r") as file:
        pass

def handle_exit(receivedData):
    os._exit(0)

handleFunctions = {
    "1": handle_manage,
    "2": handle_reports,
    "3": handle_feedback,
    "4": UpdateProfile,
    "5": handle_exit
}

def home_layer(receivedData):
    enhancer.waitingFunction()
    while True:
        print(f"\nWelcome {receivedData[1].title()}, What would you like to do?\n")
        print("1. Manage staffs - Manager, Chef (Add, Edit, Delete)")
        print("2. View sales report based on month, chef etc.")
        print("3. View feedback sent by customers.")
        print("4. Update your own profile.")
        print("5. Logout and exit.")
        userInput = input("\nEnter the number --> ")
        if int(userInput) <= 5:
            handleFunctions[userInput](receivedData)
        else:
            enhancer.InvalidOption()