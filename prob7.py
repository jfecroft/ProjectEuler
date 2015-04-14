"""
solve problem 7
"""
from prime_factorisation import is_prime


def get_primes(number):
    """
    return prime number in order
    """
    while True:
        if is_prime(number):
            yield number
        number += 1


MAX_NUM = 10001

PRIME_GEN = get_primes(1)
for i in range(MAX_NUM):
    HighPrime = PRIME_GEN.next()

print HighPrime
