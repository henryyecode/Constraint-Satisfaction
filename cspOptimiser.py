from cspProblem import *
from cspConsistency import *
from searchProblem import *
from searchGeneric import *
from display import *
import sys

# create list of all the possible domains our variables can take
domains = set()
domainDay = ["mon", "tue", "wed", "thu", "fri"]
domainTime = ["9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm"]
for Day in domainDay:
    for Time in domainTime:
        slot = Day + " " + Time
        domains.add(slot)


#create parameters to store in CSP_Cost
meetings = {}
constraints = []
softConstraints = {}


# functions that fulfil Hard Domains ...
def fulfil_day(meeting, day):
    for domain in meetings[meeting].copy():
        if day not in domain[:-3]:
            meetings[meeting].discard(domain)


def fulfil_time(meeting, time):
    for domain in meetings[meeting].copy():
        if time not in domain[-4:]:
            meetings[meeting].discard(domain)
        if time == "2pm" and domain.__contains__("12pm"):
            meetings[meeting].discard(domain)


def fulfil_morning(meeting):
    for domain in meetings[meeting].copy():
        if "am" not in domain[2:]:
            meetings[meeting].discard(domain)


def fulfil_afternoon(meeting):
    for domain in meetings[meeting].copy():
        if "pm" not in domain[2:]:
            meetings[meeting].discard(domain)


def fulfil_before_day(meeting, day):
    if day == "fri":
        for domain in meetings[meeting].copy():
            if domain[:3] == "fri":
                meetings[meeting].discard(domain)
    if day == "thu":
        for domain in meetings[meeting].copy():
            if domain[:3] == "fri" or domain[:3] == "thu":
                meetings[meeting].discard(domain)
    if day == "wed":
        for domain in meetings[meeting].copy():
            if domain[:3] == "fri" or domain[:3] == "thu" or domain[:3] == "wed":
                meetings[meeting].discard(domain)
    if day == "tue":
        for domain in meetings[meeting].copy():
            if domain[:3] != "mon":
                meetings[meeting].discard(domain)


def fulfil_before_time(meeting, time):
    num = int(''.join(filter(str.isdigit, time)))
    for domain in meetings[meeting].copy():
        domain_num = int(''.join(filter(str.isdigit, domain)))
        if num > 4:
            if domain_num + 1 > num or domain_num < 5:
                meetings[meeting].discard(domain)
        else:
            if domain_num + 1 > num and domain_num < 5:
                meetings[meeting].discard(domain)


def fulfil_after_day(meeting, day):
    if day == "thu":
        for domain in meetings[meeting].copy():
            if domain[:3] != "fri":
                meetings[meeting].discard(domain)
    if day == "wed":
        for domain in meetings[meeting].copy():
            if domain[:3] == "mon" or domain[:3] == "tue" or domain[:3] == "wed":
                meetings[meeting].discard(domain)
    if day == "tue":
        for domain in meetings[meeting].copy():
            if domain[:3] == "mon" or domain[:3] == "tue":
                meetings[meeting].discard(domain)
    if day == "mon":
        for domain in meetings[meeting].copy():
            if domain[:3] == "mon":
                meetings[meeting].discard(domain)


def fulfil_after_time(meeting, time):
    num = int(''.join(filter(str.isdigit, time)))
    for domain in meetings[meeting].copy():
        domain_num = int(''.join(filter(str.isdigit, domain)))
        if num > 4:
            if num + 1 > domain_num > 4:
                meetings[meeting].discard(domain)
        else:
            if num + 1 > domain_num or domain_num > 4:
                meetings[meeting].discard(domain)


def fulfil_before_daytime(meeting, day, time):
    num = int(''.join(filter(str.isdigit, time)))
    if day == "fri":
        for domain in meetings[meeting].copy():
            if domain[:3] == "fri":
                domain_num = int(''.join(filter(str.isdigit, domain)))
                if num > 4:
                    if domain_num + 1 > num or domain_num < 5:
                        meetings[meeting].discard(domain)
                else:
                    if domain_num + 1 > num and domain_num < 5:
                        meetings[meeting].discard(domain)
    if day == "thu":
        for domain in meetings[meeting].copy():
            if domain[:3] == "fri":
                meetings[meeting].discard(domain)
            if domain[:3] == "thu":
                domain_num = int(''.join(filter(str.isdigit, domain)))
                if num > 4:
                    if domain_num + 1 > num or domain_num < 5:
                        meetings[meeting].discard(domain)
                else:
                    if domain_num + 1 > num and domain_num < 5:
                        meetings[meeting].discard(domain)
    if day == "wed":
        for domain in meetings[meeting].copy():
            if domain[:3] == "fri" or domain[:3] == "thu":
                meetings[meeting].discard(domain)
            if domain[:3] == "wed":
                domain_num = int(''.join(filter(str.isdigit, domain)))
                if num > 4:
                    if domain_num + 1 > num or domain_num < 5:
                        meetings[meeting].discard(domain)
                else:
                    if domain_num + 1 > num and domain_num < 5:
                        meetings[meeting].discard(domain)
    if day == "tue":
        for domain in meetings[meeting].copy():
            if domain[:3] == "fri" or domain[:3] == "thu" or domain[:3] == "wed":
                meetings[meeting].discard(domain)
            if domain[:3] == "tue":
                domain_num = int(''.join(filter(str.isdigit, domain)))
                if num > 4:
                    if domain_num + 1 > num or domain_num < 5:
                        meetings[meeting].discard(domain)
                else:
                    if domain_num + 1 > num and domain_num < 5:
                        meetings[meeting].discard(domain)
    if day == "mon":
        for domain in meetings[meeting].copy():
            if domain[:3] != "mon":
                meetings[meeting].discard(domain)
            else:
                domain_num = int(''.join(filter(str.isdigit, domain)))
                if num > 4:
                    if domain_num + 1 > num or domain_num < 5:
                        meetings[meeting].discard(domain)
                else:
                    if domain_num + 1 > num and domain_num < 5:
                        meetings[meeting].discard(domain)


def fulfil_after_daytime(meeting, day, time):
    num = int(''.join(filter(str.isdigit, time)))
    if day == "fri":
        for domain in meetings[meeting].copy():
            if domain[:3] != "fri":
                meetings[meeting].discard(domain)
            else:
                domain_num = int(''.join(filter(str.isdigit, domain)))
                if num > 4:
                    if num + 1 > domain_num > 4:
                        meetings[meeting].discard(domain)
                else:
                    if num + 1 > domain_num or domain_num > 4:
                        meetings[meeting].discard(domain)
    if day == "thu":
        for domain in meetings[meeting].copy():
            if domain[:3] == "mon" or domain[:3] == "tue" or domain[:3] == "wed":
                meetings[meeting].discard(domain)
            if domain[:3] == "thu":
                domain_num = int(''.join(filter(str.isdigit, domain)))
                if num > 4:
                    if num + 1 > domain_num > 4:
                        meetings[meeting].discard(domain)
                else:
                    if num + 1 > domain_num or domain_num > 4:
                        meetings[meeting].discard(domain)
    if day == "wed":
        for domain in meetings[meeting].copy():
            if domain[:3] == "mon" or domain[:3] == "tue":
                meetings[meeting].discard(domain)
            if domain[:3] == "wed":
                domain_num = int(''.join(filter(str.isdigit, domain)))
                if num > 4:
                    if num + 1 > domain_num > 4:
                        meetings[meeting].discard(domain)
                else:
                    if num + 1 > domain_num or domain_num > 4:
                        meetings[meeting].discard(domain)
    if day == "tue":
        for domain in meetings[meeting].copy():
            if domain[:3] == "mon":
                meetings[meeting].discard(domain)
            if domain[:3] == "tue":
                domain_num = int(''.join(filter(str.isdigit, domain)))
                if num > 4:
                    if num + 1 > domain_num > 4:
                        meetings[meeting].discard(domain)
                else:
                    if num + 1 > domain_num or domain_num > 4:
                        meetings[meeting].discard(domain)
    if day == "mon":
        for domain in meetings[meeting].copy():
            if domain[:3] == "mon":
                domain_num = int(''.join(filter(str.isdigit, domain)))
                if num > 4:
                    if num + 1 > domain_num > 4:
                        meetings[meeting].discard(domain)
                else:
                    if num + 1 > domain_num or domain_num > 4:
                        meetings[meeting].discard(domain)


def fulfil_between(meeting, day1, time1_day2, time2):
    temp = time1_day2.split("-")
    time1 = temp[0]
    day2 = temp[1]
    fulfil_after_daytime(meeting, day1, time1)
    fulfil_before_daytime(meeting, day2, time2)


# Functions to fulfil BINARY CONSTRAINTS

def before(m1, m2):
    flag = True
    m1_day = m1.split(" ")[0]
    m1_time_temp = m1.split(" ")[1]
    m1_time = int(''.join(filter(str.isdigit, m1_time_temp)))
    m2_day = m2.split(" ")[0]
    m2_time_temp = m2.split(" ")[1]
    m2_time = int(''.join(filter(str.isdigit, m2_time_temp)))
    if m1_day == "tue":
        if m2_day == "mon":
            flag = False
    if m1_day == "wed":
        if m2_day == "mon" or m2_day == "tue":
            flag = False
    if m1_day == "thu":
        if m2_day == "mon" or m2_day == "tue" or m2_day == "wed":
            flag = False
    if m1_day == "fri":
        if m2_day != "fri":
            flag = False
    if m1_day == m2_day:
        if m1_time > 4:
            if m2_time < 5 or m2_time <= m1_time:
                flag = False
        if m1_time < 5:
            if m2_time <= m1_time or m2_time > 4:
                flag = False
    return flag


def same_day(m1, m2):
    m1_day = m1.split(" ")[0]
    m2_day = m2.split(" ")[0]
    if m1_day == m2_day:
        return True
    else:
        return False


def one_day_between(m1, m2):
    m1_day = m1.split(" ")[0]
    m2_day = m2.split(" ")[0]
    if m1_day == "mon":
        if m2_day != "wed":
            return False
    if m1_day == "tue":
        if m2_day != "thu":
            return False
    if m1_day == "wed":
        if m2_day != "mon" or m2_day != "fri":
            return False
    if m1_day == "thu":
        if m2_day != "tue":
            return False
    if m1_day == "fri":
        if m2_day != "wed":
            return False
    return True


def one_hour_between(m1, m2):
    m1_day = m1.split(" ")[0]
    m1_time_temp = m1.split(" ")[1]
    m1_time = int(''.join(filter(str.isdigit, m1_time_temp)))
    m2_day = m2.split(" ")[0]
    m2_time_temp = m2.split(" ")[1]
    m2_time = int(''.join(filter(str.isdigit, m2_time_temp)))
    if m1_day != m2_day:
        return False
    if m1_time < 5:
        m1_time = m1_time + 12
    if abs(m1_time - m2_time) != 2:
        return False
    else:
        return True

# Read Input File and Store in Relevant Data Structures

with open(sys.argv[1]) as file:
    for line in file:
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
                if len(request) == 5:
                    if request[2] == "after":
                        if request[3] in domainDay:
                            fulfil_after_day(request[1], request[3])
                        if request[3] in domainTime:
                            fulfil_after_time(request[1], request[3])
                    if request[2] == "before":
                        if request[3] in domainDay:
                            fulfil_before_day(request[1], request[3])
                        if request[3] in domainTime:
                            fulfil_before_time(request[1], request[3])
                if len(request) == 6:
                    if request[2] == "before":
                        fulfil_before_daytime(request[1], request[3], request[4])
                    if request[2] == "after":
                        fulfil_after_daytime(request[1], request[3], request[4])
                    if request[2] in domainDay:
                        fulfil_between(request[1], request[2], request[3], request[4])
            if request[-1].rstrip("\n") == "soft":
                if request[1] not in softConstraints:
                    softConstraints[request[1]] = []
                softConstraints[request[1]].append(request[2])


    # Soft Constraint Cost Functions

    def early_week(m):
        tempday = ["mon", "tue", "wed", "thu", "fri"]
        m_day = m.split(" ")[0]
        cost = tempday.index(m_day)
        return cost

    def late_week(m):
        tempday = ["mon", "tue", "wed", "thu", "fri"]
        m_day = m.split(" ")[0]
        cost = 4 - tempday.index(m_day)
        return cost

    def early_morning(m):
        temptime = ["9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm"]
        m_time = m.split(" ")[1]
        cost = temptime.index(m_time)
        return cost

    def midday(m):
        temptime = ["9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm"]
        m_time = m.split(" ")[1]
        cost = abs(3 - temptime.index(m_time))
        return cost

    def late_afternoon(m):
        temptime = ["9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm"]
        m_time = m.split(" ")[1]
        cost = 7 - temptime.index(m_time)
        return cost

# New Class Containing Cost

class Search_with_AC_from_Cost_CSP(Search_problem, Displayable):
    """A search problem with arc consistency and domain splitting

    A node is a CSP """

    def __init__(self, csp):
        self.cons = Con_solver(csp)  # copy of the CSP
        self.domains = self.cons.make_arc_consistent()
        self.csp = csp
        self.cost = 0

    def is_goal(self, node):
        """node is a goal if all domains have 1 element"""
        return all(len(node[var]) == 1 for var in node)

    def start_node(self):
        return self.domains

    def neighbors(self, node):
        """returns the neighboring nodes of node.
        """
        neighs = []
        var = select(x for x in node if len(node[x]) > 1)
        if var:
            dom1, dom2 = partition_domain(node[var])
            self.display(2, "Splitting", var, "into", dom1, "and", dom2)
            to_do = self.cons.new_to_do(var, None)
            for dom in [dom1, dom2]:
                newdoms = copy_with_assign(node, var, dom)
                cons_doms = self.cons.make_arc_consistent(newdoms, to_do)
                if all(len(cons_doms[v]) > 0 for v in cons_doms):
                    # all domains are non-empty
                    neighs.append(Arc(node, cons_doms))
                else:
                    self.display(2, "...", var, "in", dom, "has no solution")
        return neighs

    def heuristic(self, n):
        costs = {}

        if softConstraints:
            for key in softConstraints:
                constraintcount = 0
                costs[key] = -1
                for constraint in softConstraints[key]:
                    if constraint == "early-week":
                        constraintcount += 1
                        tempcost = -1
                        for variable in n[key]:
                            if constraintcount == 1:
                                if costs[key] < 0 or early_week(variable) < costs[key]:
                                    costs[key] = early_week(variable)
                            else:
                                if tempcost < 0 or early_week(variable) < tempcost:
                                    tempcost = early_week(variable)
                        if tempcost != -1:
                            costs[key] += tempcost
                    if constraint == "late-week":
                        constraintcount += 1
                        tempcost = -1
                        for variable in n[key]:
                            if constraintcount == 1:
                                if costs[key] < 0 or late_week(variable) < costs[key]:
                                    costs[key] = late_week(variable)
                            else:
                                if tempcost < 0 or late_week(variable) < tempcost:
                                    tempcost = late_week(variable)
                        if tempcost != -1:
                            costs[key] += tempcost
                    if constraint == "early-morning":
                        constraintcount += 1
                        tempcost = -1
                        for variable in n[key]:
                            if constraintcount == 1:
                                if costs[key] < 0 or early_morning(variable) < costs[key]:
                                    costs[key] = early_morning(variable)
                            else:
                                if tempcost < 0 or early_morning(variable) < tempcost:
                                    tempcost = early_morning(variable)
                        if tempcost != -1:
                            costs[key] += tempcost
                    if constraint == "midday":
                        constraintcount += 1
                        tempcost = -1
                        for variable in n[key]:
                            if constraintcount == 1:
                                if costs[key] < 0 or midday(variable) < costs[key]:
                                    costs[key] = midday(variable)
                            else:
                                if tempcost < 0 or midday(variable) < tempcost:
                                    tempcost = midday(variable)
                        if tempcost != -1:
                            costs[key] += tempcost
                    if constraint == "late-afternoon":
                        constraintcount += 1
                        tempcost = -1
                        for variable in n[key]:
                            if constraintcount == 1:
                                if costs[key] < 0 or late_afternoon(variable) < costs[key]:
                                    costs[key] = late_afternoon(variable)
                            else:
                                if tempcost < 0 or late_afternoon(variable) < tempcost:
                                    tempcost = late_afternoon(variable)
                        if tempcost != -1:
                            costs[key] += tempcost
            cost = 0
            for key in costs:
                cost += costs[key]
            return cost
        else:
            return 0

# New CLass Containing Cost

class CSP_with_Cost(CSP):
    def __init__(self, domains, constraints, softConstraints):
        self.csp = CSP.__init__(self, domains, constraints)
        self.cost = 0
        self.softConstraints = softConstraints


CSP = CSP_with_Cost(meetings, constraints, softConstraints)

searcher1 = AStarSearcher(Search_with_AC_from_Cost_CSP(CSP))

result = searcher1.search()
if result is not None:
    result = result.arc.to_node
    cost = 0
    for key in result:
        print(key + ":" + str(result[key]).replace("{'", "").replace("'}", ""))
        for constraint in softConstraints[key]:
            if constraint == "early-morning":
                cost += early_morning(str(result[key]).replace("{'", "").replace("'}", ""))
            if softConstraints[key] == "midday":
                cost += midday(str(result[key]).replace("{'", "").replace("'}", ""))
            if softConstraints[key] == "late-afternoon":
                cost += late_afternoon(str(result[key]).replace("{'", "").replace("'}", ""))
            if softConstraints[key] == "early-week":
                cost += early_week(str(result[key]).replace("{'", "").replace("'}", ""))
            if softConstraints[key] == "late-week":
                cost += late_week(str(result[key]).replace("{'", "").replace("'}", ""))

    print("cost:" + str(cost))

else:
    print("No Solution")





