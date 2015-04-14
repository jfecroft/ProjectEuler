from prime_factorisation import primes_less_than_n
from prime_factorisation import is_prime


def goldbachs_other_conjecture(number):
    """Return if goldbach other conjecture is true
    for *number*
    """
    primes = primes_less_than_n(number)
    for prime in primes:
        n = 0
        integer = 0
        while n <= number:
            n = prime + 2*integer**2
            if n == number:
                return True
            integer += 1
    return False

integer = 2
while (goldbachs_other_conjecture(integer) or
       is_prime(integer) or
       integer % 2 == 0
       ):
    integer += 1

print integer
