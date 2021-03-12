from domain import domainDay, domainTime

def sameDay(m1, m2):                            #Works
    day1I = m1.split(' ', 1)[0]
    day2I = m2.split(' ', 1)[0]
    if day1I == day2I:
        return True
    else:
        return False


def oneDayBetween(m1, m2):                      #Works
    day1I = domainDay.index(m1.split(' ')[0])
    day2I = domainDay.index(m2.split(' ')[0])
    diff = day2I - day1I
    print(m1.split()[0], day1I)
    print(m2.split()[0], day2I)

    if diff == -2 or diff == 2:
        return True
    else:
        return False


def oneHourBetween(m1, m2):                     #Works
    time1I = domainTime.index(m1.split(' ')[1])
    time2I = domainTime.index(m2.split(' ')[1])
    day1I = domainDay.index(m1.split(' ')[0])
    day2I = domainDay.index(m2.split(' ')[0])
    diff = time2I - time1I
    if day1I == day2I:
        if diff == -2 or diff == 2:
            return True
        else:
            return False
    return False

def before1(m1, m2):                             #Works
    day1I = domainDay.index(m1.split(' ')[0])
    day2I = domainDay.index(m2.split(' ')[0])
    time1I = domainTime.index(m1.split(' ')[1])
    time2I = domainTime.index(m2.split(' ')[1])
    if day1I < day2I:
        return True
    elif day1I == day2I:
        if time1I < time2I:
            return True
        else:
            return False,
    else:
        return False


def before1(schedule1, schedule2):
    """not equal value"""

    # nev = lambda x: x != val   # alternative definition
    # nev = partial(neq,val)     # another alternative definition
    def nev(x):
        return schedule1 != x

    nev.__name__ = str(schedule1) + "!="  # name of the function
    return nev


def before(schedule1, schedule2):                             #Works


    #print(schedule1, schedule2)

    day1I = schedule1.split(' ')[0]
    day2I = schedule2.split(' ')[0]
    time1I = schedule1.split(' ')[1]
    time2I = schedule2.split(' ')[1]
    if day1I < day2I:
        return True
    elif day1I == day2I:
        if time1I < time2I:
            return True
        else:
            return False,
    else:
        return False


