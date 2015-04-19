"""Solves project euler problem 1."""
UPPER_LIMIT = 1000
print sum(x for x in range(UPPER_LIMIT) if x % 3 == 0 or x % 5 == 0)
