__author__ = 'Stephen'
import cPickle as pickle
from parityClasses import team
from os import listdir


def findCycleOfParity(team, teamsRemaining, cycleList, endTarget, teamList):
    del teamsRemaining[team]
    if len(teamsRemaining) == 0:
        if endTarget in teamList[team].conquests:
            print "Cycle found!"
            cycleList.append(endTarget)
            return cycleList
    for conquest in teamList[team].conquests:
        if conquest in teamsRemaining:
            cycleList.append(conquest)
            test =  findCycleOfParity(conquest, dict(teamsRemaining), list(cycleList), endTarget, teamList)
            if test != None:
                return test
            else:
                cycleList.pop()


def makeLeague():
    while True:
        teamNum = raw_input("How many teams are in the league?\n> ")
        try:
            teamNum = int(teamNum)
            if teamNum < 2:
                continue
            else:
                break
        except ValueError:
            print 'Bad user! BAD!'

    teamList = {}
    for el in xrange(teamNum):
        teamList[raw_input("What's the name of team number %d?\n> " % (el + 1))] = team()

    for el in teamList:
        while True:
            inNum = raw_input("How many teams has team %s beat?\n> " % el)
            try:
                inNum = int(inNum)
                break
            except ValueError:
                print 'no'
        for el2 in xrange(inNum):
            while True:
                searchKey = raw_input('What is the name of a beaten team?\n> ')
                if searchKey in teamList.iterkeys() and searchKey != el:
                    teamList[el].addConquests(searchKey)
                    print "%s added to %s's conquests." %(searchKey, el)
                    break
                else:
                    print 'try again.'
    return teamList


def loadLeague():
    loadList = listdir('saves')
    print "The saves available are:"
    for el in xrange(len(loadList)):
        print "%d. %s" %(el + 1, loadList[el][:-2])
    takes = 2
    while True:
        userNum = raw_input("Choose a number\n> ")
        if userNum.isdigit() and 0 < int(userNum) <= len(loadList):
            teamList = pickle.load(open("saves/%s" %loadList[int(userNum) - 1], 'rb'))
            break
        else:
            print "Take %d!" %takes
            takes += 1
    return teamList


def saveLeague(teamList):
    while True:
        saveChoice = raw_input("Save this league? y/n\n> ")
        if saveChoice == 'y':
            pickle.dump(teamList, open('saves/%s.p'%raw_input("Choose a name for your league.\n> "), 'wb'))
            break
        elif saveChoice == 'n':
            break
        else:
            print 'exsqueeze me?!?'


def printCycleOfParity(cycleList):
    try:
        for el in xrange(len(cycleList)-1):
            print "%s beat %s" %(cycleList[el], cycleList[el + 1])
    except TypeError:
        print 'no cycle found'


def printTable(teamList):
    print "Here's the league table!"
    table = []
    for name, stats in teamList.iteritems():
        table.append((name, stats))

    table.sort(key=lambda x: x[1].points, reverse = True)

    for el in xrange(len(table)):
        print '%d. %s - %d'%(el+1, table[el][0], table[el][1].points)


def intro():

    while True:
        userChoice = raw_input("""Welcome to Stephen's 'Cycle of Parity' Generator Program!
Press 'm' to make your own league, 'l' to load a saved league, or 'p' to use the Premiership at week 13 of 2015.
> """)

        if userChoice == 'm':
            teamList = makeLeague()
            saveLeague(teamList)
            break
        elif userChoice == 'p':
            teamList = pickle.load(open('saves/premiership - 2015 - week13.p','rb'))
            break
        elif userChoice == 'l':
            teamList = loadLeague()
            break
        else:
            print"Let's try that again!"
    return teamList


teamList = intro()
cycleList = findCycleOfParity(teamList.keys()[0], dict(teamList), [teamList.keys()[0]], teamList.keys()[0], teamList)
printCycleOfParity(cycleList)
printTable(teamList)