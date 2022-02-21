from calendar import month
import sys
sys.stdin = open("phytonEducation/firstStep/part2/static/dateTimeTask.txt", "r")


import datetime

def addDaysToDate(date, days):
    delta = date + datetime.timedelta(days)
    print(delta.year, delta.month, delta.day)
    print(delta.strftime('%Y %#m %#d'))
    #unix# print(delta.strftime('%Y %-m %-d'))


year, month, day = [int(x) for x in (input().split())]
dateStart = datetime.date(year, month, day)

daysAdd = int(input())

addDaysToDate(dateStart, daysAdd)

