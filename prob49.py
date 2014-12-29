from PrimeFactorisation import is_prime

characters = lambda x: sorted(list(str(x)))

for a in xrange(1000, 10000):
    for b in xrange(1, (10000-a)/2+1):
        if (is_prime(a) and is_prime(a+b) and is_prime(a+b+b) and
            characters(a) == characters(a+b) == characters(a+b+b)):
                print a, a+b, a+b+b
