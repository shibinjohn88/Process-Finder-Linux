
import datetime
def findTime(daysBefore):
    # find time before the number of days in variable <Days>

    #Calculate current time
    currentTime = datetime.datetime.now()

    #Finding old time based on days before
    dateRange = datetime.timedelta(days=daysBefore)
    pointTime = currentTime -  dateRange
    unixTime = pointTime.timestamp()
    return unixTime


findTime(10)
