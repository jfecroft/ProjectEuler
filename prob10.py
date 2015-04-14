import numpy as np
from math import sqrt
NumMax = 2000000


def primes_less_than_n(NumMax):
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


PrimesList = primes_less_than_n(NumMax)
PrimesList = np.array(PrimesList)
print np.sum(PrimesList)
