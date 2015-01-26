"""Solution to project Euler problem 27."""

from PrimeFactorisation import is_prime
from itertools import product


def consecutive_solutions(a, b):
    """Return the number of consective primes
    given by n**2 + a*n + b for *a* and *b* starting from
    n = 0.
    """
    n = 0
    while is_prime(n**2 + a*n + b):
        n += 1
    return n - 2  # -2 accounts for 0 and extra n += 1 in while loop.


A_MAX = 1000
B_MAX = 1000

maximum = 0

for a, b in product(xrange(-A_MAX+1, A_MAX), xrange(-B_MAX+1, B_MAX)):
    test_maximum = consecutive_solutions(a, b)
    if test_maximum > maximum:
        maximum = test_maximum
        ab = (a, b)

print ab[0]*ab[1]
