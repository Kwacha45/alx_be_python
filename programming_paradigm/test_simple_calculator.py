import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        # Initialize a SimpleCalculator object before each test
        self.calc = SimpleCalculator()

    def test_addition(self):
        # Test normal addition
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        # Test normal subtraction
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiplication(self):
        # Test normal multiplication
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-1, 5), -5)

    def test_division(self):
        # Test normal division
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(-10, 5), -2)

        # Test divide by zero, which should raise an exception
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

    def tearDown(self):
        # Clean up (if necessary) after each test
        pass

if __name__ == "__main__":
    unittest.main()
