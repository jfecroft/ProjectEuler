"""
project euler problem 112
"""
from itertools import izip, tee

def bouncy(num):
    """
    return if a number is bouncy
    """
    num = str(num)
    less = False
    more = False
    for i, j in pairwise(num):
        if i < j:
            less = True
        elif j < i:
            more = True
        if less and more:
            return True
    return False


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)


def main():
    """
    main
    """
    num = 1
    bouncy_nums = 0
    while not bouncy_nums*100 == num*99:
        num += 1
        if bouncy(num):
            bouncy_nums += 1
    print num

if __name__ == "__main__":
    main()
