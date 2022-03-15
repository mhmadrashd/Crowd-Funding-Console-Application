from ConLog import getLastLog
import datetime


def insertNewProj(title, details, total, startDate, endDate):
    try:  # if file exist
        # try to open file
        with open("ProjectsDB.txt", "r") as dbfile:
            list = dbfile.readlines()
            # Check if file is empty or not
            if len(list) > 0:
                lastProj = list[len(list) - 1]
                projId = int(lastProj[0]) + 1
            else:
                projId = 1
    except:
        projId = 1

    dataNow = datetime.datetime.now()
    stringDate = dataNow.strftime("%d/%b/%Y, %H.%M.%S")
    # Convert project info to list
    projList = [str(projId), title, details, total, startDate, endDate, getLastLog(), stringDate]
    projInfo = ":".join(projList)
    projInfo = projInfo.strip("\n")
    data = f"{projInfo}\n"
    try:
        with open("ProjectsDB.txt", "a") as dbfile:
            dbfile.write(data)
    except:
        with open("ProjectsDB.txt", "w") as dbfile:
            dbfile.write(data)
    print("#########################\n#########################\nProject Data Inserted "
          "Successfully\n-------------------------")
    return


def searchProj(proj):
    try:
        with open("ProjectsDB.txt", "r") as dbfile:
            allProj = dbfile.readlines()
            resultProj = []
            for currProj in allProj:
                currProj = currProj.strip("\n")
                projInfo = currProj.split(":")
                if projInfo[1] == proj or projInfo[2] == proj or projInfo[3] == proj or projInfo[4] == proj or projInfo[
                    5] == proj:
                    resultProj.append(currProj)
            return resultProj
    except Exception as e:
        print(e)


def viewAllProj():
    try:
        with open("ProjectsDB.txt", "r") as dbfile:
            allProj = dbfile.readlines()
            resultProj = []
            for currProj in allProj:
                currProj = currProj.strip("\n")
                resultProj.append(currProj)
            return resultProj
    except Exception as e:
        print(e)


def DeleteProj(column, proj):
    column = str(column)
    colNum = 0
    match column:
        case "title":  # Title
            colNum = 1
        case "details":  # Details
            colNum = 2
        case "total":  # Total
            colNum = 3
        case "startDate":  # Start Date
            colNum = 4
        case "endDate":  # End Date
            colNum = 5
        case "id":  # End Date
            colNum = 0

    try:
        resultProj = []
        with open("ProjectsDB.txt", "r") as dbfile:
            permUser = getLastLog()
            allProj = dbfile.readlines()
            for currProj in allProj:
                currProj = currProj.strip("\n")
                projInfo = currProj.split(":")
                if permUser == projInfo[6]:
                    if projInfo[colNum] != proj:
                        resultProj.append(currProj)
                else:
                    resultProj.append(currProj)
        with open("ProjectsDB.txt", "w") as dbwFile:
            for currRes in resultProj:
                projInfo = currRes.strip("\n")
                data = f"{projInfo}\n"
                dbwFile.write(data)
    except Exception as e:
        print(e)


def editProj(column, id, newData):
    column = str(column)
    colNum = 0
    match column:
        case "title":  # Title
            colNum = 1
        case "details":  # Details
            colNum = 2
        case "total":  # Total
            colNum = 3
        case "startDate":  # Start Date
            colNum = 4
        case "endDate":  # End Date
            colNum = 5
        case "id":  # End Date
            colNum = 0

    try:
        resultProj = []
        with open("ProjectsDB.txt", "r") as dbfile:
            permUser = getLastLog()
            allProj = dbfile.readlines()
            for currProj in allProj:
                currProj = currProj.strip("\n")
                projInfo = currProj.split(":")
                if permUser == projInfo[6]:
                    if projInfo[colNum] == id:
                        projInfo[colNum] = newData
                        newProjInfo = ":".join(projInfo)
                        newProjInfo = newProjInfo.strip("\n")
                        currProj = newProjInfo
                resultProj.append(currProj)
        with open("ProjectsDB.txt", "w") as dbwFile:
            for currRes in resultProj:
                projInfo = currRes.strip("\n")
                data = f"{projInfo}\n"
                dbwFile.write(data)
    except Exception as e:
        print(e)


# insertNewProj("Mohamed", "Rashed", "m@gmail.com", "123", "01005294515")
# print(editProj("details", "Rashed", "ra"))