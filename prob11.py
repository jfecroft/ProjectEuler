import numpy as np

grid = np.loadtxt('prob11.txt', dtype='int')
index_iterator = np.nditer(grid, flags=['multi_index'])
number_adjacent = 4

maximum = 0

while not index_iterator.finished:
    index = index_iterator.multi_index
    sub_grid = grid[index[0]:index[0]+number_adjacent, index[1]:index[1]+number_adjacent]
    if (number_adjacent, number_adjacent) == np.shape(sub_grid): # To account for corners.
        up =  np.prod(sub_grid[:,0])
        along =  np.prod(sub_grid[0,:])
        diag1 =  np.prod(np.diag(sub_grid))
        diag2 =  np.prod(np.diag(sub_grid[::-1]))
        if np.amax((up, along, diag1, diag2)) > maximum:
            maximum = np.amax((up, along, diag1, diag2))
    index_iterator.iternext()

print maximum 
