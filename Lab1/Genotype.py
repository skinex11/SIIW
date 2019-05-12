import random


class Genotype:
    def createRoute(self, cityList):
        route = random.sample([c.id for c in cityList], len(cityList))
        return route

    def rankRoute(self, cityList):
        # route jest listą intów zawierających ID miast
        rank = 0
        iteration = 0
        for i in range(0, len(self.route)):
            city1 = cityList[self.route[i]]
            try:
                city2 = cityList[self.route[i + 1]]
            except IndexError:
                city2 = cityList[self.route[0]]
            rank += city1.calculateDistance(city2)
            iteration += 1
        return 1/rank

    def __init__(self, cityList=None, genotype=None, rank=None):
        if genotype is None and rank is None:
            self.route = self.createRoute(cityList)
            self.rank = self.rankRoute(cityList)
        elif genotype is not None:
            self.route = genotype
            self.rank = self.rankRoute(cityList)
        else:
            self.rank = rank

    def __repr__(self):
        route = ("Genotype: "+str(self.route))
        rank = ("Rank: "+str(self.rank))
        return route+'\n'+rank
