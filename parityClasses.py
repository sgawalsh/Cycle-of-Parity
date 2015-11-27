__author__ = 'Stephen'

class team:

    def __init__(self):
        self.conquests = []
        self.points = 0

    def addConquests(self, conquest):
        self.conquests.append(conquest)
        self.points += 3
