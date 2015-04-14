"""
solve problem 10
"""
import numpy as np
from prime_factorisation import primes_less_than_n
MAX_NUM = 2000000

# pylint: disable=E1103

PRIMES_LIST = primes_less_than_n(MAX_NUM)
PRIMES_LIST = np.array(PRIMES_LIST)
print np.sum(PRIMES_LIST)
