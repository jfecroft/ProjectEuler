"""
python solution to problem 15
"""

from collatz import memoize

@memoize  # takes forever without
def lattice_paths(coords):
    if coords == (0, 0):
        return 1
    paths = 0
    if coords[0] != 0:
        paths += lattice_paths((coords[0] - 1, coords[1]))
    if coords[1] != 0:
        paths += lattice_paths((coords[0], coords[1] - 1))
    return paths

print lattice_paths((20, 20))
        
