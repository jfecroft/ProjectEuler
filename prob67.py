from prob18 import max_route
from cProfile import run
FILEN = "p067_triangle.txt"

def load_file(filen):
    with open(filen) as ofile:
        pyramid = ofile.readlines()
    pyramid = [line.split() for line in pyramid]
    pyramid = [tuple([int(i) for i in line]) for line in pyramid]
    return tuple(pyramid)

print max_route(load_file(FILEN))
