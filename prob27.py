"""Solution to project Euler problem 27."""

from prime_factorisation import is_prime
from itertools import product


def consecutive_solutions(aaa, bbb):
    """Return the number of consective primes
    given by n**2 + a*n + b for *aaa* and *bbb* starting from
    n = 0.
    """
    num = 0
    while is_prime(num**2 + aaa*num + bbb):
        num += 1
    return num - 2  # -2 accounts for 0 and extra n += 1 in while loop.


A_MAX = 1000
B_MAX = 1000

MAXIMUM = 0

for a, b in product(xrange(-A_MAX+1, A_MAX), xrange(-B_MAX+1, B_MAX)):
    test_maximum = consecutive_solutions(a, b)
    if test_maximum > MAXIMUM:
        MAXIMUM = test_maximum
        ab = (a, b)

print ab[0]*ab[1]
