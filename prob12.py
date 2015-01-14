from PrimeFactorisation import PrimeFactors
import itertools
import numpy as np


def get_combintions(lst):
    combs = []
    for i in xrange(1, len(lst)+1):
        els = [list(x) for x in itertools.combinations(lst, i)]
        combs.extend(els)
    return combs


def generate_triangle_numbers():
    i = 0
    tri = 0
    while True:
        i += 1
        tri += i
        yield tri


triangle_number_generator = generate_triangle_numbers()
number_of_factors = 0
while number_of_factors < 500:
    triangle_number = triangle_number_generator.next()
    Factors = PrimeFactors(triangle_number)
    combintions = get_combintions(Factors)
    combintions = [np.prod(i) for i in combintions]
    number_of_factors = len(set(combintions))

print triangle_number
