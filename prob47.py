"""
solution to pe problem 47
"""
from prime_factorisation import prime_factors


def distinct_primes(num):
    """
    The first `num` consecutive numbers to have `num` distinct prime factors
    """
    distinct_factors = []
    i = 0
    while len(distinct_factors) != num**2:
        i += 1
        factors = [prime_factors(x) for x in range(i, i+num)]
        distinct_factors = {x for factor in factors for x in factor}
    print i

if __name__ == "__main__":
    distinct_primes(4)
