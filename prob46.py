"""
solve project euler problem 46
"""
from prime_factorisation import primes_less_than_n
from prime_factorisation import is_prime


def goldbachs_other_conjecture(number):
    """Return if goldbach other conjecture is true
    for *number*
    """
    primes = primes_less_than_n(number)
    for prime in primes:
        num = 0
        iii = 0
        while num <= number:
            num = prime + 2*iii**2
            if num == number:
                return True
            iii += 1
    return False

INUM = 2
while (goldbachs_other_conjecture(INUM) or is_prime(INUM) or
       INUM % 2 == 0):
    INUM += 1

print INUM
