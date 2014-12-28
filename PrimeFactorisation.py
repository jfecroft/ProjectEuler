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


def ProperDivisors(n):
    """Return the proper divisors of *n*."""
    PF = PrimeFactors(n)
    PD = list(powerset(PF))
    PD = [t for t in PD if t != ()]  # remove the empty set
    for i, j in enumerate(PD):
        PD[i] = np.prod(np.array(j))
    PD = set(PD)
    PD.remove(n)
    return PD


def PrimeFactors(n, PrimesList=None):
    """returns the prime factorisation of *n*."""
    if PrimesList is None:
        PrimesList = []
    if n == 1:
        return []  # account for empty set for 1
    i = 2
    while n % i != 0 and i < n:
        i += 1
    if i > 1:
        PrimesList.append(i)
    if i < n:
        return PrimeFactors(n/i, PrimesList)
    else:
        PrimesList.append(1)
        return PrimesList


def PrimesLessThanN(NumMax):
    """Return primes less than *NumMax*."""
    PrimesList = []
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
            PrimesList.append(i)
    return PrimesList
