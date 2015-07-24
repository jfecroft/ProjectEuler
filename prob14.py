"""
solutions to problem 14
"""

from collatz import collatz

MAX = 0
MAX_NUM = 1000000
for i in xrange(2, MAX_NUM):
    CollatzList = collatz(i, None)
    length = len(CollatzList)
    if length > MAX:
        Max = length
        StartNum = CollatzList[0]

print StartNum, Max
