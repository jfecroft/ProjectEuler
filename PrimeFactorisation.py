import numpy as np

from SetOperations import powerset
from math import sqrt


def is_prime(number):
    """Checks if *number* is prime."""
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


def get_proper_divisors(n):
    """Return the proper divisors of *n*."""
    prime_factors = PrimeFactors(n)
    proper_divisors = powerset(prime_factors)
    proper_divisors.remove(())
    for i, j in enumerate(proper_divisors):
        proper_divisors[i] = np.prod(np.array(j))
    proper_divisors = set(proper_divisors)
    proper_divisors.remove(n)
    return proper_divisors


def PrimeFactors(n, primes_list=None):
    """returns the prime factorisation of *n*."""
    if primes_list is None:
        primes_list = []
    if n == 1:
        return []  # account for empty set for 1
    i = 2
    while n % i != 0 and i < n:
        i += 1
    if i > 1:
        primes_list.append(i)
    if i < n:
        return PrimeFactors(n/i, primes_list)
    else:
        primes_list.append(1)
        return primes_list


def PrimesLessThanN(NumMax):
    """Return primes less than *NumMax*."""
    primes_list = []
    Primes = [True]*NumMax
    i = 2
    while i < sqrt(NumMax):
        if Primes[i] is True:
            j = i**2
            while j < NumMax:
                Primes[j] = False
                j += i
        i += 1

    for i in range(2, len(Primes)):
        if Primes[i] is True:
            primes_list.append(i)
    return primes_list
