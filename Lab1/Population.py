##klasa Population przechowuje aktualną populacje i metody związane z jej wymianą
import random

import numpy as np

from Genotype import Genotype


def generatePopulation(popSize, cityList):
    population = np.zeros(popSize, dtype=Genotype)
    for i in range(0, popSize):
        gen = Genotype(cityList)
        population[i] = gen
    return population


class Population:
    def __init__(self, popSize=None, cityList=None, population=None):
        if population is None:
            self.population = generatePopulation(popSize, cityList)
        else:
            self.population = population
