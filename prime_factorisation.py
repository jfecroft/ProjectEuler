"""
prime number methods
"""

import numpy as np
from set_operations import powerset
from math import sqrt

# pylint: disable=E1103


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


def get_proper_divisors(num):
    """Return the proper divisors of *num*."""
    proper_divisors = powerset(prime_factors(num))
    proper_divisors.remove(())
    for i, j in enumerate(proper_divisors):
        proper_divisors[i] = np.prod(np.array(j))
    proper_divisors = set(proper_divisors)
    proper_divisors.remove(num)
    return proper_divisors


def prime_factors(num, primes_list=None):
    """returns the prime factorisation of *n*."""
    if primes_list is None:
        primes_list = []
    if num == 1:
        return []  # account for empty set for 1
    i = 2
    while num % i != 0 and i < num:
        i += 1
    if i > 1:
        primes_list.append(i)
    if i < num:
        return prime_factors(num/i, primes_list)
    else:
        primes_list.append(1)
        return primes_list


def primes_less_than_n(num):
    """Return primes less than *num*."""
    primes_list = []
    primes = [True]*num
    i = 2
    while i < sqrt(num):
        if primes[i] is True:
            j = i**2
            while j < num:
                primes[j] = False
                j += i
        i += 1

    for i in range(2, len(primes)):
        if primes[i] is True:
            primes_list.append(i)
    return primes_list
