"""Run to perform unittests for the prime_factorisation module."""
import unittest
from collatz import collatz


class TestCollatz(unittest.TestCase):
    """
    Unitesting class for collatz calculations
    """
    def test_collatz(self):
        """unittest prime_factorisation.is_prime()"""
        self.assertEqual(collatz(6), [6, 3, 10, 5, 16, 8, 4, 2, 1])
        self.assertEqual(collatz(19),
                         [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13,
                          40, 20, 10, 5, 16, 8, 4, 2, 1])
