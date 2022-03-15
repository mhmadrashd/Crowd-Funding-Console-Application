def insertNewlog(email, date):
    try:  # if file exist
        # try to open file
        with open("log.txt", "r") as dbfile:
            list = dbfile.readlines()
            # Check if file is empty or not
            if len(list) > 0:
                lastlog = list[len(list) - 1]
                logId = int(lastlog[0]) + 1
            else:
                logId = 1
    except:
        logId = 1

    # Convert log info to list
    logList = [str(logId), email, date]
    logInfo = ":".join(logList)
    logInfo = logInfo.strip("\n")
    data = f"{logInfo}\n"
    try:
        with open("log.txt", "a") as dbfile:
            dbfile.write(data)
    except:
        with open("log.txt", "w") as dbfile:
            dbfile.write(data)
    return


def getLastLog():
    try:  # if file exist
        # try to open file
        with open("log.txt", "r") as dbfile:
            llist = dbfile.readlines()
            # Check if file is empty or not
            if len(llist) > 0:
                llastlog = llist[len(llist) - 1]
                llastlog = llastlog.strip("\n")
                listLastLog = llastlog.split(":")
                logmail = listLastLog[1]
            else:
                logmail = "error"
            return logmail
    except:
        return "error"

