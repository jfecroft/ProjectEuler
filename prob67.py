from prob18 import max_route
FILEN = "p067_triangle.txt"

def load_file(filen):
    """
    load file for prob 18
    """
    with open(filen) as ofile:
        pyramid = ofile.readlines()
    pyramid = [line.split() for line in pyramid]
    pyramid = [tuple([int(i) for i in line]) for line in pyramid]
    return tuple(pyramid)

print max_route(load_file(FILEN))
