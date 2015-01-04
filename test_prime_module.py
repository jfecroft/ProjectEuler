import unittest
import PrimeFactorisation


class TestPrimeFunctions(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(PrimeFactorisation.is_prime(997))

    def test_get_proper_divisors(self):
        self.assertEqual(PrimeFactorisation.get_proper_divisors(77),
                         set((1, 7, 11)))

    def test_prime_factorisation(self):
        self.assertEqual(PrimeFactorisation.PrimeFactors(999),
                         [3, 3, 3, 37, 1])


if __name__ == '__main__':
    unittest.main()
