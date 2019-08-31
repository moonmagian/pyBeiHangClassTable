#!/usr/bin/python
from datetime import time, datetime, timedelta
from ics import Event, Calendar
import re
import xlrd
import pytz
import config
import onlineGetter
TZ = pytz.timezone("Asia/Shanghai")
_CLASSTIME = [
    (time(8, 0), time(9, 35)),
    (time(9, 50), time(11, 25)),
    (time(14, 0), time(15, 35)),
    (time(15, 50), time(17, 25)),
    (time(19, 0), time(20, 35)),
    (time(20, 40), time(22, 15)),
]
BEGIN_DATE = datetime(2019, 2, 25)
if ('beginDate' in config.CONFIG.keys()):
    BEGIN_DATE = datetime.strptime(config.CONFIG['beginDate'], "%Y-%m-%d")


def GetWeekDate(beginDate, week, day):
    delta = timedelta(days=day, weeks=week - 1)
    return beginDate + delta


def CombineDateAndTime(date, t):
    return datetime(date.year, date.month, date.day, t.hour,
                    t.minute).astimezone(TZ)


def CreateClassEvents(classn, dayn, classStr):
    events = []
    name = re.findall(".*?(?=</br>)", classStr)
    # print(name[0])
    if config.CONFIG['regexMode'] == 1:
        timeMatches = re.finditer(
            r'(?P<teachername>[\u4e00-\u9fa5 \t0-9()（）]*?)\[(?P<begindate>\d*)-?(?P<enddate>\d*)\] ?周(</br>)?(?P<location>.*?)(?=$|,|，|</br>|<br/>)',
            classStr)
    elif config.CONFIG['regexMode'] == 2:
        timeMatches = re.finditer(
            r'(?P<classname>[\u4e00-\u9fa5 \t0-9()（）]*?)</br>(?P<teachername>[\u4e00-\u9fa5 \t0-9]*?)\[(?P<begindate>\d*)-?(?P<enddate>\d*)\] ?周(</br>)?(?P<location>.*)\n',
            classStr)
    else:
        timeMatches = re.finditer(config.CONFIG['customRegex'], classStr)
    teacherName = ''
    for timeMatch in timeMatches:
        timeMatch = timeMatch.groupdict()
        print(name[0])
        print(timeMatch)
        print('--------')
        rg = None
        if (timeMatch['teachername'] != ''):
            teacherName = timeMatch['teachername']
        if (timeMatch['enddate'] == ''):
            rg = range(int(timeMatch['begindate']),
                       int(timeMatch['begindate']) + 1)
        else:
            rg = range(int(timeMatch['begindate']),
                       int(timeMatch['enddate']) + 1)
        for i in rg:
            event = Event()
            event.name = name[0] if name[0] else timeMatch['classname']
            event.begin = CombineDateAndTime(GetWeekDate(BEGIN_DATE, i, dayn),
                                             _CLASSTIME[classn][0])
            event.end = CombineDateAndTime(GetWeekDate(BEGIN_DATE, i, dayn),
                                           _CLASSTIME[classn][1])
            event.location = timeMatch['location']
            event.description = "讲师：" + teacherName
            events.append(event)
    return events


def CreateClassTable():
    print("Creating calendar...")
    print('--------')
    with xlrd.open_workbook("table.xls") as xls:
        with open("classCal.ics", 'w') as calfile:
            cal = Calendar()
            sheet = xls.sheet_by_index(0)
            for classn, classes in enumerate(range(2, 8)):
                for dayn, days in enumerate(range(2, 9)):
                    if (sheet.cell_value(classes, days) != ''):
                        events = CreateClassEvents(
                            classn, dayn, sheet.cell_value(classes, days))
                        for event in events:
                            cal.events.add(event)
            calfile.writelines(cal)

    print("Success! Please check your classes carefully!")


print("pyBeiHangCalendarGenerator by MagicalMoon")
r = onlineGetter.GetClassTable()
if (r):
    CreateClassTable()
    print("The class calendar has been saved as classCal.ics")
else:
    print("Failed to create class table")
