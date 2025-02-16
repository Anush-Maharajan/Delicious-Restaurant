import enhancer
import os

def handle_manage(receivedData):
    userData = enhancer.give_User_list()
    print((userData))
    pass

def handle_reports(receivedData):

    pass

def handle_feedback(receivedData):
    with open("feedbacks.txt", "r") as file:
        pass

def handle_profile(receivedData):
    print("What changes do you want to make?")
    print("1. Change name.")
    print("2. Change email.")
    print("2. Change password.")
    promptInput = input("\nEnter the number --> ")
    handle_change[promptInput](receivedData)

def handle_exit(receivedData):
    os._exit(0)

handleFunctions = {
    "1": handle_manage,
    "2": handle_reports,
    "3": handle_feedback,
    "4": handle_profile,
    "5": handle_exit
}

def change_name(receivedData):
    userID, name, password, role = receivedData
    changeName = input("Enter the name to change: ")
    confirmation = input("Are you sure you want to change the name?\n[y/n] --> ")
    if changeName and confirmation.lower() == "y":
    
        userData = enhancer.give_User_list()

        for user in userData:
            if userID == user[0]:
                user[1] = changeName

        enhancer.update_User_list(userData)

        print("\nName Changed Sucessfully!\n")
    else:
        print("Name change is cancelled")
            

def change_password(receivedData):
    userID, name, password, role = receivedData
    old_password = input("Enter the old password: ")
    new_password = input("Enter the new password: ")
    if password == old_password and new_password:
        userData = enhancer.give_User_list()
        for user in userData:
            if userID == user[2]:
                user[2] = new_password
        
        enhancer.update_User_list(userData)
        
        print("password change Sucessful!")
    
    else:
        print("Wrong password or invalid new password")

handle_change = {
    "1": change_name,
    "2": change_password
}

def home_layer(receivedData):
    enhancer.waitingFunction()
    while True:
        print(f"Welcome {receivedData[1].title()}, What would you like to do?\n")
        print("1. Manage staffs - Manager, Chef (Add, Edit, Delete)")
        print("2. View sales report based on month, chef etc.")
        print("3. View feedback sent by customers.")
        print("4. Update your own profile.")
        print("5. Logout and exit.")
        userInput = input("\nEnter the number --> ")
        handleFunctions[userInput](receivedData)