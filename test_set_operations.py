"""
unittests for the set_operation module.
"""
import unittest
import set_operations


# pylint: disable=R0903
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

        self.assertEqual(set_operations.powerset(['x', 'y', 'z']),
                         xyz_powerset)


if __name__ == '__main__':
    unittest.main()
