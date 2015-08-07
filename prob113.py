
from prob112 import bouncy
import cProfile


def main():
    i = 0
    bouncy_nums = 0
    while i < 10**6:
        if not bouncy(i):
            bouncy_nums += 1
        i += 1

cProfile.run('main()')
    
