from cspProblem import CSP, Constraint

# create list of all the possible domains our variables can take
domains = []
domainDay = ["mon", "tue", "wed", "thu", "fri"]
domainTime = ["9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm"]
for Day in domainDay:
    for Time in domainTime:
        slot = Day + " " + Time
        domains.append(slot)

#create parameters to store in CSP
meetings = {}
constraints = []


def before(domain1, domain2):
    #TODO
    return 1


def same_day(domain1, domain2):
    #TODO
    return 1


def one_day_between(domain1, domain2):
    #TODO
    return 1


def one_hour_between(domain1, domain2):
    #TODO
    return 1


def fulfil_day(meeting, day):
    for domain in meetings[meeting][:]:
        if day not in domain[:-3]:
            meetings[meeting].remove(domain)


def fulfil_time(meeting, time):
    for domain in meetings[meeting][:]:
        if time not in domain[-4:]:
            meetings[meeting].remove(domain)
        if time == "2pm" and domain.__contains__("12pm"):
            meetings[meeting].remove(domain)


def fulfil_morning(meeting):
    for domain in meetings[meeting][:]:
        if "am" not in domain[2:]:
            meetings[meeting].remove(domain)


def fulfil_afternoon(meeting):
    for domain in meetings[meeting][:]:
        if "pm" not in domain[2:]:
            meetings[meeting].remove(domain)


with open("sample.txt") as file:
    for line in file:                                                          #Split file into lines
        request = []
        for word in line.split(" "):
            request.append(word.rstrip(","))
        if request[0] == "meeting":
            meetings[request[1].rstrip("\n")] = domains.copy()
        if request[0] == "constraint":
            if request[2] == "before":
                constraint = Constraint((request[1], request[-1].strip()), before)
                constraints.append(constraint)
            if request[2] == "same-day":
                constraint = Constraint((request[1], request[-1].strip()), same_day)
                constraints.append(constraint)
            if request[2] == "one-day-between":
                constraint = Constraint((request[1], request[-1].strip()), one_day_between)
                constraints.append(constraint)
            if request[2] == "one-hour-between":
                constraint = Constraint((request[1], request[-1].strip()), one_hour_between)
                constraints.append(constraint)
        if request[0] == "domain":
            if request[-1].rstrip("\n") == "hard":
                if len(request) == 4:
                    if request[2] in domainDay:
                        fulfil_day(request[1], request[2])
                    if request[2] in domainTime:
                        fulfil_time(request[1], request[2])
                    if request[2] == "morning":
                        fulfil_morning(request[1])
                    if request[2] == "afternoon":
                        fulfil_afternoon(request[1])


CSP = CSP(meetings, constraints)

print(CSP.domains)
print(CSP.constraints)












