import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        # Initialize a SimpleCalculator object before each test
        self.calc = SimpleCalculator()

    def test_add(self):
        # Test normal addition
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        # Test normal subtraction
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiply(self):
        # Test normal multiplication
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self
