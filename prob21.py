from prime_factorisation import get_proper_divisors
import numpy as np


def proper_divisor_sum(integer):
    """Return the sum of the proper divisors of *n*."""
    proper_divisors = np.array(list(get_proper_divisors(integer)))
    return np.sum(proper_divisors)

LOW, HIGH = 2, 10000  # start at 2 to avoid empty set for proper divisors for 1
sum_divisors = [proper_divisor_sum(x) for x in xrange(LOW, HIGH + 1)]

sum_amicable_numbers = 0
for i, j in enumerate(sum_divisors):
    if (i+LOW < j and j-LOW >= 0 and j-LOW <= len(sum_divisors)-1 and
            sum_divisors[j-LOW] == i+LOW):
        sum_amicable_numbers += i+LOW
        sum_amicable_numbers += j

print sum_amicable_numbers
