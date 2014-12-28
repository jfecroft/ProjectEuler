from PrimeFactorisation import is_prime
from itertools import product


def quadratic_formula(a, b, n):
    return is_prime(n**2 + a*n + b)


def consecutive_solutions(a, b):
    prime_test = True
    n = 0
    while prime_test is True:
        prime_test = quadratic_formula(a, b, n)
        n += 1
    return n - 2


A_MAX = 1000
B_MAX = 1000

maximum = 0

for a, b in product(xrange(-A_MAX+1, A_MAX), xrange(-B_MAX+1, B_MAX)):
    test_maximum = consecutive_solutions(a, b)
    if test_maximum > maximum:
        maximum = test_maximum
        ab = (a, b)

print ab[0]*ab[1]
