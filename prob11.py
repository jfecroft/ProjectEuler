import numpy as np
Grid = np.loadtxt('prob11.txt',dtype='int')
print np.shape(Grid)
it = np.nditer(Grid, flags=['multi_index'])
num = 4

Max = 0

while not it.finished:
 index = it.multi_index
 SubGrid = Grid[index[0]:index[0]+num,index[1]:index[1]+num]
 if (num,num) == np.shape(SubGrid):
  up    =  np.prod(SubGrid[:,0])
  along =  np.prod(SubGrid[0,:])
  diag1 =  np.prod(np.diag(SubGrid))
  diag2 =  np.prod(np.diag(SubGrid[::-1]))
  if up    > Max:Max = up
  if along > Max:Max = along
  if diag1 > Max:Max = diag1
  if diag2 > Max:Max = diag2
 it.iternext()

print Max 
