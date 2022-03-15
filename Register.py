import re
import Main
import conDB

regexEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def checkValidMail(email):
    if re.fullmatch(regexEmail, email):
        return False
    else:
        return True


def checkValidPhone(ph):
    if re.findall("01.{9}", ph):
        return True
    else:
        return False


def registoPage():
    print("############################\nWelcome to Register Page\n0-To back main menu\n############################")
    fName = input("Enter Your First Name: ")
    if fName == "0":
        return Main.main()
    while len(fName) == 0 or (not fName.isalpha()):
        fName = input("You Must Enter Valid First Name\nEnter Your First Name: ")

    lName = input("Enter Your Last Name: ")
    while len(lName) == 0 or (not lName.isalpha()):
        lName = input("You Must Enter Valid Last Name\nEnter Your Last Name: ")

    email = input("Enter Your Email: ")
    while checkValidMail(email):
        email = input("You Must Enter Valid Email\nEnter Your Email: ")

    password = input("Enter Your Password: ")
    while len(password) < 8:
        password = input("Please Enter more than 8 char\nEnter Your Password: ")

    repassword = input("Enter Your rePassword: ")
    while repassword != password:
        repassword = input("Please Enter Same Password\nEnter Your rePassword: ")

    phone = input("Enter Your Phone: ")
    while not checkValidPhone(phone):
        phone = input("Please Enter Valid Phone\nEnter Your Phone: ")

    return conDB.insertNewUser(fName, lName, email, password, phone)
