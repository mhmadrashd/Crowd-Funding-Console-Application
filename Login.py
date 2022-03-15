import Main
import datetime
from HomeMenu import homeMenuPage
from Register import checkValidMail
from conDB import chkValidUser
from ConLog import insertNewlog


def loginPage():
    print("############################\nWelcome to Login Page\n0-To back main menu\n############################")
    email = input("Enter Your Email: ")
    if email == "0":
        return Main.main()

    while checkValidMail(email):
        email = input("Enter Valid Email\nEnter Your Email: ")

    password = input("Enter Your Password: ")
    while len(password) < 8:
        password = input("You Must Enter Valid Password\nEnter Your Password: ")

    if chkValidUser(email, password):
        dataNow = datetime.datetime.now()
        strDate = dataNow.strftime("%d/%b/%Y, %H.%M.%S")
        insertNewlog(email, strDate)
        return homeMenuPage()
    else:
        print("Invalid Data")
        return loginPage()

