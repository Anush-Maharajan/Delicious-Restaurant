import time
import os
import platform

def waitingFunction():
    for i in range(7):
        print("." * i, "\r", end = "")
        time.sleep(0.233471)
    os.system("cls" if platform.system() == "Windows" else "clear")

def give_User_list():
    userData = []
    with open("Database/user.txt", "r") as file:
        for row in file.readlines(): 
            id, prev_name, email, actual_password, role = row.strip().split(';')
            userData.append([id, prev_name, email, actual_password, role])

    return userData

def update_User_list(userData):
    with open("Database/user.txt", "w") as file:
        for user in userData:
            file.write(";".join(user) + "\n")

def userID_increment():
    with open("Database/user.txt", "r") as file:
        lines = file.readlines()
        lastLine = lines[-1] if lines else ""
        lastID = int(lastLine.strip().split(";")[0]) + 1

    return lastID

def InvalidOption():
    # print("Error Occured: enter a valid option")
    print("""
▒█▀▀▀ █▀▀█ █▀▀█ █▀▀█ █▀▀█ 　 █▀▀█ █▀▀ █▀▀ █░░█ █▀▀█ █▀▀█ █▀▀ █▀▀▄ ▄ 　 ░▀░ █▀▀▄ ▀█░█▀ █▀▀█ █░░ ░▀░ █▀▀▄ 
▒█▀▀▀ █▄▄▀ █▄▄▀ █░░█ █▄▄▀ 　 █░░█ █░░ █░░ █░░█ █▄▄▀ █▄▄▀ █▀▀ █░░█ ░ 　 ▀█▀ █░░█ ░█▄█░ █▄▄█ █░░ ▀█▀ █░░█ 
▒█▄▄▄ ▀░▀▀ ▀░▀▀ ▀▀▀▀ ▀░▀▀ 　 ▀▀▀▀ ▀▀▀ ▀▀▀ ░▀▀▀ ▀░▀▀ ▀░▀▀ ▀▀▀ ▀▀▀░ ▀ 　 ▀▀▀ ▀░░▀ ░░▀░░ ▀░░▀ ▀▀▀ ▀▀▀ ▀▀▀░ 

█▀▀█ █▀▀█ ▀▀█▀▀ ░▀░ █▀▀█ █▀▀▄ 
█░░█ █░░█ ░░█░░ ▀█▀ █░░█ █░░█ 
▀▀▀▀ █▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀▀ ▀░░▀""")


if __name__ == "__main__":
    InvalidOption()