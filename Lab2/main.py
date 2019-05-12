import cProfile
import sys

import numpy as np

from backtracking import solveBackTracking
from forward import forwardChecking

#global N
#N = 5

def main():
    N = int(sys.argv[1])
    #board = np.zeros((N, N), dtype=int)
    board2 = np.zeros((N, N), dtype=int)
    # solveBackTracking(board, 0, N)
    # print("Backtracking: ")
    # print(board)
    # print("--------------------------")
    # print("Forward checking: ")
    forwardChecking(board2, 0, N, )


if __name__ == '__main__':
    cProfile.run('main()', sort='time', )
