##klasa city przechowuje parametry dot. miast
import numpy as np


class City:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def calculateDistance(self, city):
        xDistance = abs(self.x - city.x)
        yDistance = abs(self.y - city.y)
        #print(xDistance, yDistance)
        distance = np.sqrt((xDistance ** 2) + (yDistance ** 2))
        return distance

    def __repr__(self):
        id = str(self.id)
        x = str(self.x)
        y = str(self.y)
        return str('City(index:' + id + ', x:' + x + ', y:' + y + ')\n')
