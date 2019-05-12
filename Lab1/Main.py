# program wywoławczy
import cProfile

from City import City
from Genotype import Genotype
from Population import Population
import numpy as np
import matplotlib.pyplot as plt

popSize = 200
genSize = range(0, 100)
tour = 5
px = 0.7
pm = 0.01


def readCities():
    path = "data/hard_0.txt"
    cities = [City(0, 0, 0)]
    with open(path, 'r') as file:
        content = file.readlines()
        for line in content:
            row = line.split('\t')
            id = int(row[0])
            x = float(row[1])
            y = float(row[2])
            cities.append(City(id, x, y))
    file.close()

    return cities


def selectGenotypes(population, popSize, tour):
    selectedGenotypes = np.zeros(popSize * 2, dtype=Genotype)
    iteration = 0
    while iteration < 2 * popSize:
        maxRank = Genotype(None, None, 0)
        indexes = []
        while len(indexes) < tour:
            i = np.random.randint(0, popSize)
            if i not in indexes:
                p = population.population[i]
                indexes.append(i)
                if len(indexes) == 1:
                    maxRank = p
                elif p.rank > maxRank.rank:
                    maxRank = p
        selectedGenotypes[iteration] = maxRank
        iteration += 1
    return selectedGenotypes


def breed(parent1, parent2):
    childP1 = []

    geneA = int(np.random.random() * len(parent1.route))
    geneB = int(np.random.random() * len(parent1.route))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1.route[i])

    childP2 = [item for item in parent2.route
               if item not in childP1]

    child = childP1 + childP2
    return child


def mutate(genotype):
    r = np.random.randint(len(genotype.route), size=2)
    genotype.route[r[0]], genotype.route[r[1]] = genotype.route[r[1]], genotype.route[r[0]]
    return genotype


def generatePopulation(population, popSize, cityList, tour, px, pm):
    result = np.zeros(popSize, dtype=Genotype)
    selectedGenotypes = selectGenotypes(population, popSize, tour)
    parentIndex = 0

    for i in range(0, popSize):
        toBreed = np.random.rand()
        toMutate = np.random.rand()
        if toBreed > px != 0:
            result[i] = selectedGenotypes[parentIndex]
        else:
            genotype = breed(selectedGenotypes[parentIndex], selectedGenotypes[parentIndex + 1])
            result[i] = Genotype(cityList, genotype)
        if toMutate < pm != 0:
            mutate(result[i])
        parentIndex += 2
        i += 1
    return Population(None, None, result)


def startGA():
    cityList = readCities()

    population1 = Population(popSize, cityList)

    maxRank = []
    minRank = []
    avgRank = []

    for i in genSize:
        population1 = generatePopulation(population1, popSize, cityList, tour, px, pm)
        avg = []
        maxLocal = 0
        minLocal = 10000
        for genotype in population1.population:
            if genotype.rank > maxLocal:
                maxLocal = genotype.rank
            elif genotype.rank < minLocal:
                minLocal = genotype.rank
            avg.append(genotype.rank)
        maxRank.append(maxLocal)
        minRank.append(minLocal)
        avgRank.append(sum(avg) / len(avg))
        print("Population " + str(i) + "/" + str(len(genSize)))
    return maxRank, minRank, avgRank


# for i in range(0, 1):
#     maxRank, minRank, avgRank = startGA()
#     print(max(maxRank), min(minRank), np.average(avgRank))

cProfile.run('startGA()',sort = 'tottime')

plt.plot(maxRank, 'r')
plt.plot(minRank, 'b')
plt.plot(avgRank, 'y')
plt.legend(['Najlepsza ocena', 'Najgorsza ocena', 'Średnia ocena'])
plt.title('')
plt.show()
