#The aquarium is keeping track of visitors using unlimited visit cards.
#The have a list, which contains one list per unlimited card customer.
#Each customer list shows which dates in July they visited the aquarium.
#(For example here - the first card holding customer visited 02/07/20 and 06/07/20)
visitDates = [[2, 6], [1, 3, 6, 10], [15, 17, 22, 29], [23], [1, 8, 11, 14, 15, 22, 29], [1, 2, 14]]

#Write a function that tells us how many card holding visitors the aquarium has had
#Write a function that gives us a list of dates card holding visitors went to the aquarium ( combine lists and remove duplicates)
#Write a function that tells us which dates *no* card holders visited the aquarium
#Write a function that tells us the maximum visits one visitor made (ie The longest list of dates)
#Write a function the minimum visits (ie. the shortest list of dates)

def visitorCount():
    return(len(visitDates))

def dateList():
    combinedList =[]
    for visitor in visitDates:
        for day in visitor:
            if day not in combinedList:
                combinedList.append(day)
    combinedList.sort()
    return combinedList

def noVisit():
    noVisitList =[]
    july = list(range(1, 31))
    visited = dateList()
    for x in july:
        if x not in visited:
            noVisitList.append(x)
    return noVisitList
        
def busiestVisitor():
    mostVisits = 0
    busiestVisitorsList = []
    for visitor in visitDates:
        if len(visitor) > mostVisits:
            mostVisits= len(visitor)
            busiestVisitorsList = visitor
    return busiestVisitorsList

def infrequentVisitor():
    leastVisits = 1000000
    infrequentVisitorsList = []
    for visitor in visitDates:
        if len(visitor) < leastVisits:
            leastVisits= len(visitor)
            infrequentVisitorsList = visitor
    return infrequentVisitorsList


print(visitorCount())
print(dateList())
print(noVisit())
print(busiestVisitor())
print(infrequentVisitor())
