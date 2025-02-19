import UTILs.enhancer as enhancer

def UpdateProfile(receivedData):
    print("What changes do you want to make?")
    print("1. Change name.")
    print("2. Change email.")
    print("2. Change password.")
    promptInput = input("\nEnter the number --> ")
    handle_change[promptInput](receivedData)

def change_name(receivedData):
    userID = receivedData[0]
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
        print("\nName change is cancelled\n")
            

def change_password(receivedData):
    userID, password= receivedData[0], receivedData[3]
    old_password = input("Enter the old password: ")
    new_password = input("Enter the new password: ")
    if password == old_password and new_password:
        userData = enhancer.give_User_list()
        passwordChange = False
        for user in userData:
            if userID == user[0]:
                user[3] = new_password
                passwordChange = True
        
        if passwordChange:
            enhancer.update_User_list(userData)
            print("\nPassword change Sucessful!")
        else:
            print("Wrong password or invalid new password")
    
    else:
        print("Wrong password or invalid new password")

handle_change = {
    "1": change_name,
    "2": change_password
}