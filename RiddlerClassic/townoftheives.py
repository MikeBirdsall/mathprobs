from random import randrange
from operator import add

class town(object):

    def __init__(self, houses, first=100):
        self.houses = houses
        self.first = first
        self.cash = [first] * houses

    def run(self):
        self.clear()
        houses = self.houses
        for house in range(houses):
            robbed = randrange(houses)
            while robbed == house:
                robbed = randrange(houses)
            self.cash[house] += self.cash[robbed]
            self.cash[robbed] = 0

    def clear(self):
        self.cash = [self.first] * self.houses

    def average(self, runs=100):
        total = [0]*self.houses
        for dummy in range(runs):
            self.run()
            # print "Sum of run is %s" % sum(self.cash)
            total = map(add, total, self.cash)
        print float(runs), sum(total)
        self.avg = [float(z)/float(runs) for z in total]


    def answer(self):
        return self.cash


