__author__ = 'Stephen'
import cPickle as pickle
from parityClasses import team

#while True:
#    teamNum = raw_input("How many teams are in the league?")
#    try:
#        teamNum = int(teamNum)
#        if teamNum < 2:
#            continue
#        else:
#            break
#    except ValueError:
#        print 'Bad user! BAD!'
#
#teamList = {}
#for el in xrange(teamNum):
#    teamList[raw_input("What's the name of team number %d?" % (el + 1))] = team()

teamList = pickle.load(open('prem - teamlist.p', 'rb'))

for el in teamList:
    while True:
        inNum = raw_input("How many teams has team %s beat?" % el)
        try:
            inNum = int(inNum)
            break
        except ValueError:
            print 'no'
    for el2 in xrange(inNum):
        while True:
            searchKey = raw_input('What is the name of a beaten team?')
            if searchKey in teamList.iterkeys() and searchKey != el:
                teamList[el].addConquests(searchKey)
                print "%s added to %s's conquests." %(searchKey, el)
                break
            else:
                print 'try again.'


pickle.dump(teamList, open('premiership - 2015 - week13.p', 'wb'))
