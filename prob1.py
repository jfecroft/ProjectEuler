"""Solves project euler problem 1."""
UPPER_LIMIT = 1000


def multiple_of_three_or_five(num):
    """Ruturn if *num* is a multiple of 3 or 5."""
    if num % 3 == 0:
        return True
    elif num % 5 == 0:
        return True
    else:
        return False

sum_multiples = 0
for i in range(1, UPPER_LIMIT):
    if multiple_of_three_or_five(i):
        sum_multiples += i

print sum_multiples
