"""
solve problem 3
"""

PRIME = 600851475143


def largest_prime_factor(num):
    """ Return the largest prime factor of n."""
    i = 2
    while num % i != 0 and i < num:
        i += 1
    if i < num:
        return largest_prime_factor(num/i)
    else:
        return num

print largest_prime_factor(PRIME)
