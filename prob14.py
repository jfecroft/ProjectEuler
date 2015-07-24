"""
solutions to problem 14
"""

from collatz import collatz

MAXIMUM = 0
MAX_NUM = 1000000
for i in xrange(2, MAX_NUM):
    collatz_list = collatz(i)
    length = len(collatz_list)
    if length > MAXIMUM:
        MAXIMUM = length
        start_num = collatz_list[0]

print start_num, MAXIMUM
print collatz(start_num)
