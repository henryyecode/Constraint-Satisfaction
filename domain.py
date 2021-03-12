totalDomain = ["mon 9am", "mon 10am", "mon 11am", "mon 12pm", "mon 1pm", "mon 2pm", "mon 3pm", "mon 4pm",
               "tue 9am", "tue 10am", "tue 11am", "tue 12pm", "tue 1pm", "tue 2pm", "tue 3pm", "tue 4pm",
               "wed 9am", "wed 10am", "wed 11am", "wed 12pm", "wed 1pm", "wed 2pm", "wed 3pm", "wed 4pm",
               "thu 9am", "thu 10am", "thu 11am", "thu 12pm", "thu 1pm", "thu 2pm", "thu 3pm", "thu 4pm",
               "fri 9am", "fri 10am", "fri 11am", "fri 12pm", "fri 1pm", "fri 2pm", "fri 3pm", "fri 4pm"]

domainDay = ["mon", "tue", "wed", "thu", "fri"]
domainTime = ["9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm"]

#Hard Domains

def getDays(day):
    daysDomain = set()
    for scedule in totalDomain:
        for word in scedule.split():
            if word == day:
                daysDomain.add(scedule)

    return daysDomain


def getTimes(time):
    timeDomain = set()
    for scedule in totalDomain:
        for word in scedule.split():
            if word == time:
                timeDomain.add(scedule)

    return timeDomain


def getDaysBefore(day):

    newDayDomain = set()
    dayIndex = domainDay.index(day)
    i = 0

    while i < dayIndex:
        day = domainDay[i]
        for schedule in totalDomain:
            for word in schedule.split():
                if word == day:
                    newDayDomain.add(schedule)

        i += 1
    return newDayDomain

def getTimesBefore(time):

    newTimeDomain = set()
    timeIndex = domainTime.index(time)
    i = 0

    while i < timeIndex:
        time = domainTime[i]
        for schedule in totalDomain:
            for word in schedule.split():
                if word == time:
                    newTimeDomain.add(schedule)
        i += 1
    return newTimeDomain



def getDomainBefore(day, time):

    newTotalDomain = set()
    timeIndex = domainTime.index(time)
    dayIndex = domainDay.index(day)
    i = 0

    while i < dayIndex:
        dayI = domainDay[i]
        for schedule in totalDomain:
            for word in schedule.split():
                if word == dayI:
                    newTotalDomain.add(schedule)
        i += 1

    i = 0
    temp = []
    while i < timeIndex:
        for schedule in totalDomain:
            for word in schedule.split():
                if word == day:
                    temp.append(schedule)
        i += 1

    i = 0
    for schedule in temp:
        for word in schedule.split():
            if word in domainTime:
                if domainTime.index(word) < timeIndex:
                    newTotalDomain.add(schedule)
    return newTotalDomain

def getDaysAfter(day):
    newDayDomain = set()
    dayIndex = domainDay.index(day)

    while dayIndex < 5:
        day = domainDay[dayIndex]
        for scedule in totalDomain:
            for word in scedule.split():
                if word == day:
                    newDayDomain.add(scedule)
        dayIndex += 1
    return newDayDomain

def getTimesAfter(time):
    newTimeDomain = set()
    timeIndex = domainTime.index(time)

    while timeIndex < 8:
        time = domainTime[timeIndex]
        for scedule in totalDomain:
            for word in scedule.split():
                if word == time:
                    newTimeDomain.add(scedule)
        timeIndex += 1
    return newTimeDomain

def getDomainAfter(day, time):
    newTotalDomain = set()
    timeIndex = domainTime.index(time)
    dayIndex = domainDay.index(day)
    i = dayIndex
    temp = 0

    while i < 5:
        dayI = domainDay[i]
        for schedule in totalDomain:
            for word in schedule.split():
                if word in domainDay:
                    if domainDay.index(word) > domainDay.index(day):
                        if schedule not in newTotalDomain:
                            newTotalDomain.add(schedule)
        i += 1

    i = 0;
    flag = 0

    for schedule in totalDomain:
        for word in schedule.split():
            if word == day:
                flag = 1
                temp = schedule
            elif flag == 1:
                if domainTime.index(word) >= timeIndex:
                    newTotalDomain.add(schedule)
                flag = 0

    return newTotalDomain

def getDomainBetween(day1, time1, day2, time2):
    list1 = getDomainAfter(day1, time1)
    list2 = getDomainBefore(day2, time2)
    return set(set(list1) & set(list2))


#Soft Domains
def earlyWeekA(m1):
    day = m1[0].split()[1]
    dayIndex = domainDay.index(m1[0])
    cost = dayIndex
    return cost

def earlyWeek(schedule):
    day = schedule.split()[0]
    dayIndex = domainDay.index(day)
    cost = dayIndex
    return cost


def lateWeekA(m1):
    dayIndex = domainDay.index(m1[0])
    cost = 4 - dayIndex  # Friday is at index 5 in domainDay
    return cost

def lateWeek(schedule):
    day = schedule.split()[0]
    dayIndex = domainDay.index(day)
    cost = 4 - dayIndex
    return cost

def earlyMorningA(m1):
    timeIndex = domainTime.index(m1[1])
    cost = timeIndex
    return cost

def earlyMorning(schedule):
    time = schedule.split()[1]
    timeIndex = domainTime.index(time)
    cost = timeIndex
    return cost

def lateAfternoon(m1):
    timeIndex = domainDay.index(m1[1])
    cost = 7 - timeIndex  # 4pm is index 7 in domainTime
    return cost

def lateAfternoon(schedule):
    time = schedule.split()[1]
    timeIndex = domainTime.index(time)
    cost = 7 - timeIndex  # 4pm is index 7 in domainTime
    return cost


def middayA(m1):
    timeIndex = domainTime.index(m1[1])
    cost = abs(timeIndex - 3)  # 12pm is index 3, subtract then find absolute value for cost
    return cost

def midday(schedule):
    time = schedule.split()[1]
    timeIndex = domainTime.index(time)
    return abs(timeIndex - 3)
    #cost = abs(time - 3)  # 12pm is index 3, subtract then find absolute value for cost
    #return cost

def totalCost(csp, constraints):
    cost = 0
    for constraint in constraints:
        if constraint == "before":
            print("TEST")