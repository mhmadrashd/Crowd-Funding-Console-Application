import Main
import ConProj


def homeMenuPage():
    print("############################\n\tWelcome to Home Page\n############################")
    print(
        "\t1-View All Projects\n\t2-Insert New Project\n\t3-Edit Project\n\t4-Delete Project\n\t"
        "5-Search In Projects\n\t0-To back main menu")
    menuNum = input("############################\nEnter Number of your choice: ")
    if menuNum == "0":
        return Main.main()

    while not menuNum.isdigit():
        menuNum = input("Please Enter Valid Number\nEnter Number of your choice: ")
    menuNum = int(menuNum)
    match menuNum:
        case 1:  # All Projects
            print(ConProj.viewAllProj())
        case 2:  # Insert New Project
            InsertProjPage()
        case 3:  # Edit Project
            chooseColumn("edit")
        case 4:  # Delete Project
            chooseColumn("delete")
        case 5:  # Search In Projects
            projSrch = input("0-To Back\nEnter Data: ")
            if projSrch == "0":
                return homeMenuPage()
            while len(projSrch) == 0:
                projSrch = input("You Must Enter Valid Data\nEnter Data: ")
            print(ConProj.searchProj(projSrch))
        case 0:  # Back to main menu
            return Main.main()
        case _:
            print("----------------------------")
            print("Enter Valid Number")
            print("----------------------------")
            return homeMenuPage()
    return homeMenuPage()


def chooseColumn(operation):
    print("\t1-Title\n\t2-Details\n\t3-Total\n\t4-Start Date\n\t5-End Date\n\t6-Project ID\n\t0-To back main menu")
    column = input("############################\nEnter Number of your choice: ")
    if column == "0":
        return homeMenuPage()

    while not column.isdigit():
        column = input("Please Enter Valid Number\nEnter Number of your choice: ")

    column = int(column)
    match column:
        case 1:  # Title
            if operation == "edit":
                data = input("Enter Old Title Data: ")
                while len(data) == 0:
                    data = input("Please Enter Valid Data\nEnter Old Title Data: ")

                newData = input("Enter New Title Data: ")
                while len(newData) == 0:
                    newData = input("Please Enter Valid Data\nEnter New Title Data: ")

                return ConProj.editProj("title", data, newData)
            else:
                data = input("Enter Title Data: ")
                while len(data) == 0:
                    data = input("Please Enter Valid Data\nEnter Title Data: ")
                return ConProj.DeleteProj("title", data)
        case 2:  # Details
            if operation == "edit":
                data = input("Enter Old Details Data: ")
                while len(data) == 0:
                    data = input("Please Enter Valid Data\nEnter Old Details Data: ")

                newData = input("Enter New Details Data: ")
                while len(newData) == 0:
                    newData = input("Please Enter Valid Data\nEnter New Details Data: ")

                return ConProj.editProj("details", data, newData)
            else:
                data = input("Enter Details Data: ")
                while len(data) == 0:
                    data = input("Please Enter Valid Data\nEnter Details Data: ")
                return ConProj.DeleteProj("details", data)
        case 3:  # Total
            if operation == "edit":
                data = input("Enter Old Total Data: ")
                while len(data) == 0:
                    data = input("Please Enter Valid Data\nEnter Old Total Data: ")

                newData = input("Enter New Total Data: ")
                while len(newData) == 0:
                    newData = input("Please Enter Valid Data\nEnter New Total Data: ")

                return ConProj.editProj("total", data, newData)
            else:
                data = input("Enter Total Data: ")
                while len(data) == 0:
                    data = input("Please Enter Valid Data\nEnter Total Data: ")
                return ConProj.DeleteProj("total", data)
        case 4:  # Start Date
            if operation == "edit":
                data = input("Enter Old Start Date Data: ")
                while len(data) == 0:
                    data = input("Please Enter Valid Data\nEnter Old Start Date Data: ")

                newData = input("Enter New Start Date Data: ")
                while len(newData) == 0:
                    newData = input("Please Enter Valid Data\nEnter New Start Date Data: ")

                return ConProj.editProj("startDate", data, newData)
            else:
                data = input("Enter Start Date Data: ")
                while len(data) == 0:
                    data = input("Please Enter Valid Data\nEnter Start Date Data: ")
                return ConProj.DeleteProj("startDate", data)
        case 5:  # End Date
            if operation == "edit":
                data = input("Enter Old End Date Data: ")
                while len(data) == 0:
                    data = input("Please Enter Valid Data\nEnter Old End Date Data: ")

                newData = input("Enter New End Date Data: ")
                while len(newData) == 0:
                    newData = input("Please Enter Valid Data\nEnter New End Date Data: ")

                return ConProj.editProj("endDate", data, newData)
            else:
                data = input("Enter End Date Data: ")
                while len(data) == 0:
                    data = input("Please Enter Valid Data\nEnter End Date Data: ")
                return ConProj.DeleteProj("endDate", data)
        case 6:  # Project ID
            if operation == "edit":
                data = input("Enter Old Project ID Data: ")
                while len(data) == 0:
                    data = input("Please Enter Valid Data\nEnter Old Project ID Data: ")

                newData = input("Enter New Project ID Data: ")
                while len(newData) == 0:
                    newData = input("Please Enter Valid Data\nEnter New Project ID Data: ")

                return ConProj.editProj("id", data, newData)
            else:
                data = input("Enter Project ID Data: ")
                while len(data) == 0:
                    data = input("Please Enter Valid Data\nEnter Project ID Data: ")
                return ConProj.DeleteProj("id", data)
        case 0:  # Back to main menu
            return Main.main()
        case _:
            print("----------------------------")
            print("Enter Valid Number")
            print("----------------------------")
            return homeMenuPage()


def InsertProjPage():
    print("############################\nWelcome to Info Project Page\n0-To back main "
          "menu\n############################")
    projTitle = input("Enter Title: ")
    if projTitle == "0":
        return homeMenuPage()
    while len(projTitle) == 0:
        projTitle = input("You Must Enter Valid Title\nEnter Title: ")

    projDetails = input("Enter Project Details: ")
    while len(projDetails) == 0:
        projDetails = input("You Must Enter Valid Project Details\nEnter Project Details: ")

    projTotal = input("Enter Total Target: ")
    while not projTotal.isdigit():
        projTotal = input("You Must Enter Valid Total Target\nEnter Total Target: ")

    projStartDate = input("Enter Start Date: ")
    while len(projStartDate) != 10:
        projStartDate = input("Please Enter Valid Date\nEnter Start Date: ")

    projEndDate = input("Enter End Date: ")
    while len(projEndDate) != 10:
        projEndDate = input("Please Enter Valid Date\nEnter End Date: ")

    ConProj.insertNewProj(projTitle, projDetails, projTotal, projStartDate, projEndDate)
    print("############################\nProject Date Inserted Successfully\n--------------------------------")
    return homeMenuPage()
