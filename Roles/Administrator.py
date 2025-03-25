import UTILs.enhancer as enhancer
from UTILs.updateProfile import UpdateProfile
import os

def handle_manage(receivedData):
    print("\nWhat do you want to do?\n")
    print("1. Show all user data.")
    print("2. Edit User Data.")
    print("3. Add User Data.")
    print("4. Delete User Data.")
    print("5. Back to home page.")
    userChoice = input("Enter the number --> ")

    if userChoice == "5":
        pass
    elif userChoice:
        handle_data[userChoice]()
    else:
        enhancer.InvalidOption()
   
def data_show():
    userData = enhancer.give_User_list()
    print("\nDisplaying all the user data:\n")
    for user in userData:
        print("\t".join(user))

def data_edit():
    id_to_edit = input("Enter the user ID to edit userdata: ")
    userData = enhancer.give_User_list()
    for user in userData:
        if user[0] == id_to_edit:
            print("What do you want to edit?\n")
            print("1. Name\n2. Email\n3. password\n4. Role\n5. User ID")
            choice = input("Enter the number --> ")
            if choice:
                editOptions[choice](id_to_edit)
            else:
                enhancer.InvalidOption()

def edit_Name(editingID):
    userData = enhancer.give_User_list()
    new_name = input("Enter the new name: ")
    for user in userData:
        if user[0] == editingID:
            user[1] = new_name
            enhancer.update_User_list(userData)
            print("Name has been updated")
            break


def edit_Email(editingID):
    userData = enhancer.give_User_list()
    new_email = input("Enter the new email: ")
    for user in userData:
        if user[0] == editingID:
            user[2] = new_email
            enhancer.update_User_list(userData)
            print("Email has been updated")
            break

def edit_Password(editingID):
    userData = enhancer.give_User_list()
    new_password = input("Enter the new password: ")
    for user in userData:
        if user[0] == editingID:
            user[3] = new_password
            enhancer.update_User_list(userData)
            print("Password has been updated")
            break

def edit_Role(editingID):
    userData = enhancer.give_User_list()
    new_role = input("Enter the new role: ")
    for user in userData:
        if user[0] == editingID:
            user[4] = new_role
            enhancer.update_User_list(userData)
            print("role has been updated")
            break

def edit_UserID(editingID):
    userData = enhancer.give_User_list()
    new_userID = input("Enter the new userID: ")
    for user in userData:
        if user[0] == editingID:
            user[0] = new_userID
            enhancer.update_User_list(userData)
            print("UserID has been updated")
            break
    


editOptions = {
    "1": edit_Name,
    "2": edit_Email,
    "3": edit_Password,
    "4": edit_Role,
    "5": edit_UserID
}

def data_add():
    addData = True
    while addData:
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        role = input("Enter Role: ")
        id = enhancer.userID_increment()

        with open("Database/user.txt", "a") as file:
            file.write(f"{id};{name};{email};{password};{role}\n")

        wannaAddData = input("Do you want to add more data?[y/n]\n--> ")
        if wannaAddData.lower() == "y":
            addData = True
        elif wannaAddData.lower() == "n":
            addData = False
        else:
            enhancer.InvalidOption()

def data_delete():
    id_to_delete = input("Enter the userID to delete userdata: ")
    confirmation = input("Are you sure you want to delete?[y/n]\n--> ")
    if id_to_delete and confirmation.lower() == "y":
        userData = enhancer.give_User_list()
        userData = [user for user in userData if user[0] != id_to_delete]
        enhancer.update_User_list(userData)
        print("User data deleted sucessfully")
    else:
        print("IdNotFound: No such userID found in file")    

handle_data = {
    "1": data_show,
    "2": data_edit,
    "3": data_add,
    "4": data_delete
}

def handle_reports(receivedData):
    print("\nShowing the monthly report of this year.\n")
    with open("Database/reports.txt") as file:
        file.read()

def handle_feedback(receivedData):
    with open("Database/feedbacks.txt", "r") as file:
        feedbacks = file.readlines()
        for feedback in feedbacks:
            sno, name, userfeedback = feedback.strip().split(";")
            print(f"\n{sno}\t{name}\t{userfeedback}")

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

        if handler := handleFunctions.get(userInput, None):
           handler(receivedData)
        else:
            enhancer.InvalidOption()