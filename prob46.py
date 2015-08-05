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

def main():
    inum = 2
    while (goldbachs_other_conjecture(inum) or is_prime(inum) or
           inum % 2 == 0):
        inum += 1
    print inum

if __name__ == "__main__":
    main()
