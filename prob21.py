"""
solve problem 21
"""
from prime_factorisation import get_proper_divisors
import numpy as np


# pylint: disable=E1103


def proper_divisor_sum(integer):
    """Return the sum of the proper divisors of *n*."""
    proper_divisors = np.array(list(get_proper_divisors(integer)))
    return np.sum(proper_divisors)

LOW, HIGH = 2, 10000  # start at 2 to avoid empty set for proper divisors for 1
SUM_DIVISORS = [proper_divisor_sum(x) for x in xrange(LOW, HIGH + 1)]

SUM_AMICABLE_NUMBERS = 0
for i, j in enumerate(SUM_DIVISORS):
    if (i+LOW < j and j-LOW >= 0 and j-LOW <= len(SUM_DIVISORS)-1 and
            SUM_DIVISORS[j-LOW] == i+LOW):
        SUM_AMICABLE_NUMBERS += i+LOW
        SUM_AMICABLE_NUMBERS += j

print SUM_AMICABLE_NUMBERS
