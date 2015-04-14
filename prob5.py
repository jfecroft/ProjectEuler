"""
solve problem 5
"""


def is_multiple(num, numbers):
    """
    return if numbers are all multiples of num
    """
    return all(num % number == 0 for number in numbers)

MAX_NUMBER = 20
NUMBER = MAX_NUMBER  # Start at MAX_NUMBER.
while not is_multiple(NUMBER, range(1, MAX_NUMBER+1)):
    NUMBER += MAX_NUMBER  # Check all numbers multiples of MAX_NUMBER.

print NUMBER
