import psutil
import datetime

listOfProcessNames = []

def getListOfProcesses(createTime):
    intervalTime = findTime(createTime)
    for pro in psutil.process_iter():
        prInfoDict = pro.as_dict(attrs=['pid', 'name', 'create_time', 'username'])
        if prInfoDict['create_time'] < intervalTime:
            listOfProcessNames.append(prInfoDict)
    return

def findTime(daysBefore):
    # find time before the number of days in variable <Days>

    #Calculate current time
    currentTime = datetime.datetime.now()

    #Finding old time based on days before
    dateRange = datetime.timedelta(days=daysBefore)
    pointTime = currentTime -  dateRange
    unixTime = pointTime.timestamp()
    return unixTime

getListOfProcesses(1)
# Setting default value for 1 day

#Sort list by create time and PID
listOfProcessNames = sorted(listOfProcessNames, key = lambda i: (i['create_time'], i['pid']))

#Get values from list of processes
for currentPrcoess in listOfProcessNames:
    username = currentPrcoess["username"]
    pid = currentPrcoess["pid"]
    creationTime = currentPrcoess["create_time"]
    creationTimeString = datetime.datetime.fromtimestamp(creationTime).strftime('%d.%m.%Y %H:%M:%S')
    processName = currentPrcoess["name"]
    print("Username: %s, PID: %8i, Program: %s" % (username, pid, processName),", created on", creationTimeString)

