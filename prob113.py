"""
project euler prob 112
"""
from prob112 import bouncy
import cProfile


def main():
    """
    generate bouncy numbers
    """
    i = 0
    bouncy_nums = 0
    while i < 10**6:
        if not bouncy(i):
            bouncy_nums += 1
        i += 1

cProfile.run('main()')

