from PrimeFactorisation import is_prime 


def quadratic_formula(a, b, n):
    return is_prime(n**2 + a*n + b)


for i in xrange(50):
    print i, quadratic_formula(1, 41, i)
