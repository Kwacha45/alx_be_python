import unittest
from simple_calculator import SimpleCalculator  # Assuming simple_calculator.py is in the same directory

class TestSimpleCalculator(unittest.TestCase):

  def test_addition(self):
    calc = SimpleCalculator()  # Might be using 'calc' instead of 'calculator'
    result = calc.add(5, 3)
    self.assertEqual(result, 8)  # Using self.assertEqual(result, expected_value)

  def test_subtract(self):
    calc = SimpleCalculator()
    result = calc.subtract(10, 4)
    self.assertEqual(result, 6)

  def test_multiply(self):
    calc = SimpleCalculator()
    result = calc.multiply(2, 6)
    self.assertEqual(result, 12)

  def test_divide(self):
    calc = SimpleCalculator()

    result = calc.divide(12, 3)
    self.assertEqual(result, 4)

    with self.assertRaises(ZeroDivisionError):
      calculator.divide(10, 0)  # Might be using 'calculator' here for consistency

if __name__ == "__main__":
  unittest.main()