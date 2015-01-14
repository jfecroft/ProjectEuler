"""
solve project euler problem 25.
"""


def fib():
    """
    fibonacci number generator.
    """
    a, b = 0, 1
    while True:
        a, b = b, a+b
        yield b

number_of_digits = 1000

fib_generator = fib()
fib_number = 0
term = 1
while len(str(fib_number)) < number_of_digits:
    fib_number = fib_generator.next()
    term += 1

print term
