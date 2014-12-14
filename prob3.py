prime = 600851475143

def largest_prime_factor(n):
    """ Return the largest prime factor of n."""
    i = 2
    while (n%i != 0 and i < n):
        i += 1
    if (i < n):
        return largest_prime_factor(n/i)
    else:
        return n

print largest_prime_factor(prime)
