import Main


def insertNewUser(fname, lname, email, password, phone):
    userId = 0
    try:  # if file exist
        # try to open file
        with open("UsersDB.txt", "r") as dbfile:
            list = dbfile.readlines()
            # Check if file is empty or not
            if len(list) > 0:
                lastuser = list[len(list) - 1]
                userId = int(lastuser[0]) + 1
            else:
                userId = 1
    except:
        userId = 1
    # Convert user info to list
    userlist = [str(userId), fname, lname, email, password, phone]
    userinfo = ":".join(userlist)
    userinfo = userinfo.strip("\n")
    data = f"{userinfo}\n"
    try:
        with open("UsersDB.txt", "a") as dbfile:
            dbfile.write(data)
    except:
        with open("UsersDB.txt", "w") as dbfile:
            dbfile.write(data)
    print("#########################\n#########################\nData Inserted Successfully\n-------------------------")
    return Main.main()

def chkValidUser(email, password):
    try:
        with open("UsersDB.txt", "r") as dbfile:
            allUsers = dbfile.readlines()
            for user in allUsers:
                userInfo = user.split(":")
                if userInfo[3] == email and userInfo[4] == password:
                    return True
            return False
    except Exception as e:
        print(e)


# insertNewUser("Mohamed", "Rashed", "m@gmail.com", "123","01005294515")
#print(chkValidUser("m@gmail.com", "123"))
