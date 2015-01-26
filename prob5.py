def is_multiple(n, numbers):
    return all(n % number == 0 for number in numbers)

MAX_NUMBER = 20
number = MAX_NUMBER  # Start at MAX_NUMBER.
while not is_multiple(number, range(1, MAX_NUMBER+1)):
    number += MAX_NUMBER  # Check all numbers multiples of MAX_NUMBER.

print number
