"""
solve problem 10
"""
import numpy as np
from prime_factorisation import primes_less_than_n
MAX_NUM = 2000000

# pylint: disable=E1103

def main():
    primes_list = primes_less_than_n(MAX_NUM)
    primes_list = np.array(primes_list)
    print np.sum(primes_list)

if __name__ == "__main__":
    main()
