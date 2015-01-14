"""Run to perform unittests for the PrimeFactorisation module."""
import unittest
import SetOperations


class TestPrimeFunctions(unittest.TestCase):
    """
    Unitesting class for set_operations module.
    """

    def test_powerset(self):
        """
        unittest for powerset method.
        """

        xyz_powerset = [(),
                        ('x',),
                        ('y',),
                        ('z',),
                        ('x', 'y'),
                        ('x', 'z'),
                        ('y', 'z'),
                        ('x', 'y', 'z')]

        self.assertEqual(SetOperations.powerset(['x', 'y', 'z']), xyz_powerset)


if __name__ == '__main__':
    unittest.main()
