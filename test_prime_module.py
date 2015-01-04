import unittest
import PrimeFactorisation


class TestSequenceFunctions(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(PrimeFactorisation.is_prime(997))

    def test_get_proper_divisors(self):
        self.assertTrue(PrimeFactorisation.get_proper_divisors(77) ==
                        set((1, 7, 11)))


if __name__ == '__main__':
    unittest.main()
