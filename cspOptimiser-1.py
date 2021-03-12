
cases = 0
newmeetingsDict = {}
constraints = []
constraintsCounter = 0
domainCounter = 0

from cspProblem import CSP, Constraint
from constraint import sameDay, before, oneHourBetween, oneDayBetween
from domain import *

totalDomain = {"mon 9am", "mon 10am", "mon 11am", "mon 12pm", "mon 1pm", "mon 2pm", "mon 3pm", "mon 4pm",
               "tue 9am", "tue 10am", "tue 11am", "tue 12pm", "tue 1pm", "tue 2pm", "tue 3pm", "tue 4pm",
               "wed 9am", "wed 10am", "wed 11am", "wed 12pm", "wed 1pm", "wed 2pm", "wed 3pm", "wed 4pm",
               "thu 9am", "thu 10am", "thu 11am", "thu 12pm", "thu 1pm", "thu 2pm", "thu 3pm", "thu 4pm",
               "fri 9am", "fri 10am", "fri 11am", "fri 12pm", "fri 1pm", "fri 2pm", "fri 3pm", "fri 4pm"}

domainDay = ["mon", "tue", "wed", "thu", "fri"]
domainDayComma = {"mon,", "tue,", "wed,", "thu,", "fri,"}
domainTime = ["9am", "10am", "11am", "12am", "1pm", "2pm", "3pm", "4pm"]
domainTimeComma = {"9am,", "10am,", "11am,", "12am,", "1pm,", "2pm," "3pm,", "4pm,"}
softConstraintsTime = "none"
softConstraintsDay = "none"

def remove_comma(text):
    return text[:-1]


with open("sample.txt") as f:

    for line in f:                                                          #Split file into lines
        for word in line.split():                                                   #Split lines into words
            if word == "meeting," or cases == 'meetingVariables':           #If first word in line is meeting
                if cases == 0:
                    cases = "meetingVariables"
                elif cases == "meetingVariables":                           #Store meeting in dictionary
                    newmeetingsDict[word] = totalDomain
                    cases = 0
                    #print(newmeetingsDict[word])
            elif word == "constraint," or cases == "constraintVariables":   #If first word in line is constraint
                if cases == 0:
                    cases = "constraintVariables"
                    newConstraint = []
                    constraintsCounter += 1
                elif cases == "constraintVariables":                        #Store constraint variables in list
                    newConstraint.append(word)
                    constraintsCounter += 1
                    if constraintsCounter == 4:
                        constraintsCounter = 0
                        constraints.append(newConstraint)
                        cases = 0
            elif word == "domain," or cases == "domainVariables":           #If first word in line is domain
                if cases == 0:
                    cases = "domainVariables"
                    newDomain = []
                    domainCounter += 1

                elif cases == "domainVariables":
                    newDomain.append(word)
                    domainCounter += 1

                    if word == "hard":
                        domainCounter = 0
                        cases = 0
                        meeting = remove_comma(newDomain[0])

                        if newDomain[2] == "hard":
                            if newDomain[1] in domainDayComma:
                                day = remove_comma(newDomain[1])                         #Remoive ',' after day of week
                                newmeetingsDict[meeting] = getDays(day)
                            elif newDomain[1] in domainTimeComma:
                                time = remove_comma(newDomain[1])
                                newmeetingsDict[meeting] = getTimes(time)
                            elif newDomain[1] == "morning":
                                newmeetingsDict[meeting] = getTimesBefore("12pm")
                            elif newDomain[1] == "afternoon":
                                newmeetingsDict[meeting] = getTimesAfter("12pm")
                        elif newDomain[3] == "hard":
                            temp = newDomain[2]
                            if newDomain[1] == "before":
                                if temp in domainDayComma:
                                    day = remove_comma(newDomain[2])
                                    newmeetingsDict[meeting] = getDaysBefore(day)
                                else:
                                    time = remove_comma(newDomain[2])
                                    newmeetingsDict[meeting] = getTimesAfter(time)
                            elif newDomain[1] == "after":
                                if temp in domainDayComma:
                                    day = remove_comma(newDomain[2])
                                    newmeetingsDict[meeting] = getDaysAfter(day)

                                else:
                                    time = remove_comma(newDomain[2])
                                    newmeetingsDict[meeting] = getTimesAfter(time)
                        elif newDomain[4] == "hard":
                            if newDomain[2] not in domainDay and newDomain[2] not in domainTimeComma:
                                day1 = newDomain[1]
                                time1 = newDomain[2].split("-")[0]
                                day2 = newDomain[2].split("-")[1]
                                time2 = remove_comma(newDomain[3])

                                #print(getDomainBetween(day1, time1, day2, time2))

                            elif newDomain[1] == "before":
                                time = remove_comma(newDomain[3])
                                day = newDomain[2]
                                newmeetingsDict[meeting] = getDomainBefore(day, time)
                            else:
                                day = newDomain[2];
                                time = remove_comma(newDomain[3])
                                newmeetingsDict[meeting] = getDomainAfter(day, time)
                    elif word == "soft":
                        if newDomain[1] == "early-week,":
                            print("earlyWeek")
                        elif newDomain[1] == "late-week,":
                            print("late week")
                        elif newDomain[1] == "early-morning,":
                            print("early Morning")
                            newDomain = []
                        elif newDomain[1] == "midday":
                            print("midday")
                        elif newDomain[1] == "late-afternoon,":
                            print("lateAfternoon")


constraintList = []

from constraint import sameDay, oneDayBetween, oneHourBetween, before

for constraint in constraints:
    if constraint[1] == "before":
        C = Constraint((constraint[0], constraint[2]), before)
    elif constraint[1] == "same-day":
        C = Constraint((constraint[0], constraint[2]), sameDay)
    elif constraint[1] == "one-day-between":
        C = Constraint((constraint[0], constraint[2]), oneDayBetween)
    elif constraint[1] == "one-hour-between":
        C = Constraint((constraint[0], constraint[2]), oneHourBetween)
    constraintList.append(C)

csp1 = CSP(newmeetingsDict, constraintList)



from operator import lt,ne,eq,gt
from cspExamples import test, ne_
from searchGeneric import Searcher, AStarSearcher               #Applying AStar search on it?
from display import Displayable, visualize
from cspConsistency import Search_with_AC_from_CSP, ac_search_solver

test(ac_search_solver, csp1)









