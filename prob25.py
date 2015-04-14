"""
solve project euler problem 25.
"""


def fib():
    """
    fibonacci number generator.
    """
    aaa, bbb = 0, 1
    while True:
        aaa, bbb = bbb, aaa+bbb
        yield bbb

NUMBER_OF_DIGITS = 1000

FIB_GENERATOR = fib()
FIB_NUMBER = 0
TERM = 1
while len(str(FIB_NUMBER)) < NUMBER_OF_DIGITS:
    FIB_NUMBER = FIB_GENERATOR.next()
    TERM += 1

print TERM
