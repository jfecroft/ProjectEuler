"""
solve problem 11
"""
import numpy as np

# pylint: disable=E1103

GRID = np.loadtxt('prob11.txt', dtype='int')
INDEX_ITERATOR = np.nditer(GRID, flags=['multi_index'])
NUMBER_ADJACENT = 4

MAXIMUM = 0

while not INDEX_ITERATOR.finished:
    INDEX = INDEX_ITERATOR.multi_index
    SUB_GRID = GRID[INDEX[0]:INDEX[0]+NUMBER_ADJACENT,
                    INDEX[1]:INDEX[1]+NUMBER_ADJACENT]
    # To account for corners.
    if (NUMBER_ADJACENT, NUMBER_ADJACENT) == np.shape(SUB_GRID):
        UP = np.prod(SUB_GRID[:, 0])
        ALONG = np.prod(SUB_GRID[0, :])
        DIAG1 = np.prod(np.diag(SUB_GRID))
        DIAG2 = np.prod(np.diag(SUB_GRID[::-1]))
        if np.amax((UP, ALONG, DIAG1, DIAG2)) > MAXIMUM:
            MAXIMUM = np.amax((UP, ALONG, DIAG1, DIAG2))
    INDEX_ITERATOR.iternext()

print MAXIMUM
