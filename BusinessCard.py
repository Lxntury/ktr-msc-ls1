import os.path

def main():
    choice = ''

    # Q to quit
    while choice != 'Q' and choice != 'q':
        # Interface
        new_Step = "-"*24
        print(new_Step)
        choice = input(" - Connect (C)\n - Create a user (U)\n - Quit (Q)\n"+new_Step+"\n")
        # If a user exist, and C is pressed, the connection menu shows up
        if os.path.exists("user.txt") and (choice == 'C' or choice == 'c'):
           connection_menu()
           # U, to creat a new user
        if choice == 'U' or choice == 'u':
           new_user()

def connection_menu():
    user_file = open("user.txt","r")
    data = user_file.readlines()
    print("Type an user name, then the password")
    userPass = {}
    # all user and their password are added to userPass
    for user in data:
        index = user.find(' ')
        user_name = user[:index]
        userPass[user[:index]] = user[index+1:len(user)-1:]

        print(user_name)
    entry = input() 
    print()


    if entry not in userPass:
        print(entry+ " could not be found")
    else:
        password_entry = input("Enter "+entry+" password: ")
        if password_entry != userPass[entry]:
            print("Wrong password")
        else:
            print("You're connected")
            main_menu(entry)

    user_file.close()

def new_user():
    user_file = open("user.txt", "a")
    user_name = input("Enter a username: ")
    user_ps = input("Enter a password: ")
    user_file.write(user_name + " " + user_ps)
    user_file.write("\n")
    user_file.close()


def writeData(username, dataL):
    save_file = open(username+"save.txt", "a")
    for data in dataL:
        save_file.write(data + " ")
    save_file.write("\n")

def writeNum(username, profilN):
    save_file = open(username+"save.txt", "r")
    data = save_file.readlines()
    data[1] = "Profil Number :" + str(profilN)+"\n"
    with open(username+"save.txt", 'w') as file:
        file.writelines(data)

def add_profil_menu(username, numberProfiles):
    dataL = []
    while True:
        data = input("Enter a name ")
        # name as to be aplha
        if data.isalpha():
            dataL.append(data)
            break
    while True:
        data = input("Enter a Company name (optional)")
        # company name as to be aplha
        if data.isalpha() or not data:
            dataL.append(data)
            break
    data = input("Enter an email adress (optional) ")
    dataL.append(data)
    while True:
        data = input("Enter a telephone number (optional) ")
        # Phone number as to be numeric
        if data.isnumeric() or not data:
            dataL.append(data)
            break
    writeNum(username, numberProfiles+1)
    writeData(username, dataL)

def my_info(username):
    dataL = []
    while True:
        data = input("Enter your name ")
        if data.isalpha():
            dataL.append(data)
            break
    while True:
        data = input("Enter your Company name (optional)")
        if data.isalpha() or not data:
            dataL.append(data)
            break
    data = input("Enter your email adress (optional) ")
    dataL.append(data)
    while True:
        data = input("Enter your telephone number (optional) ")
        if data.isnumeric() or not data:
            dataL.append(data)
            break
    save_file = open(username+"save.txt", "r")
    data = save_file.readlines()
    data[0] = ""
    for info in dataL:
        data[0] += info + " "
    data[0] += "\n"
    with open(username+"save.txt", 'w') as file:
        file.writelines(data)

def main_menu(username):

    choice = ''
    # L for log out
    while choice != 'L' and choice != 'l':
        # If this username doesn't got a file, a new is created, with profil number at 0
        if not os.path.exists(username+"save.txt"):
            new_file = open(username+"save.txt", "a+")
            new_file.write("\nProfil Number :0\n")
            new_file.close()

        save_file = open(username+"save.txt","r+")
        firstLine = save_file.readline()
        secondLine = save_file.readline()
        numberProfiles = int(secondLine[15:])
        new_Step = "-"*24
        print(new_Step+"\nThere is "+str(numberProfiles)+" profiles")

        choice = input(" - My profile (M)\n - Add profile (A)\n - Show library (S)\n - Log out (L)\n"+new_Step+"\n")
        # My profile
        if choice == 'M' or choice == 'm':
            my_info(username)
        # Add profile
        if choice == 'A' or choice == 'a':
            add_profil_menu(username, numberProfiles)

        # Show library
        if numberProfiles != 0 and (choice == 'S' or choice == 's'):
            print("All added business card: ")
            for profil in save_file.readlines():
                print("---->" +profil)
        save_file.close()
    
    return 0
    
main()