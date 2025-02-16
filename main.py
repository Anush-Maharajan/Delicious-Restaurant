"""
    This is the main page where you can login into the program.
    Having various roles

"""

import Roles.Administrator as Administrator
import Roles.Manager as Manager
import Roles.Chef as Chef
import Roles.Customer as Customer
import enhancer

userData = []
loginAttempt = 1
loggedIn = False
sendingData = []

# Starting code block that will execute
def login_Main():
    login_email = input("Email: ")
    login_Password = input("Password: ")
    LoginSystem(login_email, login_Password)

def LoginSystem(email, password):
    global loggedIn, loginAttempt, sendingData

    userData = enhancer.give_User_list()
        
    for user in userData:
        if email == user[2] and password == user[3]:
            global sendingData
            sendingData = user
            welcomeUser(user[1],user[4])
            loggedIn = True
        
    if not loggedIn:
        if loginAttempt >= 3:
            print("\nMany failed attemps: Program Exited\n")
        else:
            loginRetry()
            


#codeblock that asks for id and password again in retry
def loginRetry():

    global loginAttempt
    loginAttempt+=1

    print("\nInvalid UserID or Password\nPlease Enter the email and password again\n")
    userID = input("Email: : ")
    userPassword = input("Password: ")
    LoginSystem(userID, userPassword)

def welcomeUser(name, role):
    global sendingData
    print(f"\nWelcome {name.capitalize()}! You are being redirected to your role page!\nPLease wait...\n")
    match role:
        case "admin":
            Administrator.home_layer(sendingData)
        case "manager":
            Manager.home_layer(sendingData)
        case "chef":
            Chef.home_layer(sendingData)
        case "customer":
            Customer.home_layer(sendingData)
        case _:
            print("\nIt seems you do not have a role.\nPlease inquire the manager about it.\n")

if __name__ == "__main__":
    print("Welcome to Delicious Restaurant.\nPlease enter login email and password\n")
    login_Main()