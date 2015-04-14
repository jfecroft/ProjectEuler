"""
solve problem 12
"""
from prime_factorisation import prime_factors
import itertools
import numpy as np

# pylint: disable=E1103


def get_combintions(lst):
    """
    return all cobinations of the elements in lst
    """
    combs = []
    for iii in xrange(1, len(lst)+1):
        els = [list(x) for x in itertools.combinations(lst, iii)]
        combs.extend(els)
    return combs


def generate_triangle_numbers():
    """
    return triangle numbers
    """
    iii = 0
    tri = 0
    while True:
        iii += 1
        tri += iii
        yield tri


TRIANGLE_NUMBER_GENERATOR = generate_triangle_numbers()
NUMBER_OF_FACTORS = 0
while NUMBER_OF_FACTORS < 500:
    TRIANGLE_NUMBER = TRIANGLE_NUMBER_GENERATOR.next()
    FACTORS = prime_factors(TRIANGLE_NUMBER)
    COMBINTIONS = get_combintions(FACTORS)
    COMBINTIONS = [np.prod(i) for i in COMBINTIONS]
    NUMBER_OF_FACTORS = len(set(COMBINTIONS))

print TRIANGLE_NUMBER
