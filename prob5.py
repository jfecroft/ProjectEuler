"""
solve problem 5
"""


def is_multiple(num, numbers):
    """
    return if numbers are all multiples of num
    """
    return all(num % number == 0 for number in numbers)


def main():
    """
    main
    """
    max_number = 20
    number = max_number  # Start at max_number.
    while not is_multiple(number, range(1, max_number+1)):
        number += max_number  # Check all numbers multiples of MAX_NUMBER.
    print number

if __name__ == "__main__":
    main()
