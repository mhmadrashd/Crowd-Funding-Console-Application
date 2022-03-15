import Login
import Register


def main():
    print("1-Login to system\n2-Register new account\n3-Exit")
    msg1 = input("Enter Number of your choice: ")

    while not msg1.isdigit():
        msg1 = input("Please Enter Valid Data\nEnter Number of your choice: ")
    msg1 = int(msg1)
    match msg1:
        case 1:  # Login Page
            return Login.loginPage()
        case 2:  # Register Page
            return Register.registoPage()
        case 3:  # Exit
            exit()
        case _:
            print("----------------------------")
            print("Enter Valid Number")
            print("----------------------------")
            return main()
