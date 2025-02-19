import UTILs.enhancer as enhancer
from UTILs.updateProfile import UpdateProfile
import os

def handle_manage(receivedData):
    userChoice = input("\nWhat do you want to do?\n")
    print("1. Show all user data.")
    print("2. Edit User Data.")
    print("3. Add User Data.")
    print("4. Delete User Data.")

    if userChoice:
        handle_data[userChoice]()
    else:
        print("Error Occured: Invalid option")
   
def data_show():
    userData = enhancer.give_User_list()
    print("\nDisplaying all the data users:\n")
    for user in userData:
        print("\t".join(user))


def data_add():
    pass

def data_edit():
    pass

def data_delete():
    pass

handle_data = {
    "1": data_show,
    "2": data_add,
    "3": data_edit,
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
        handleFunctions[userInput](receivedData)