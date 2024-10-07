import unittest
from simple_calculator import SimpleCalculator  # Assuming simple_calculator.py is in the same directory

class TestSimpleCalculator(unittest.TestCase):

  def test_add(self):
    calculator = SimpleCalculator()
    result = calculator.add(5, 3)
    self.assertEqual(result, 8)

  def test_subtract(self):
    calculator = SimpleCalculator()
    result = calculator.subtract(10, 4)
    self.assertEqual(result, 6)

  def test_multiply(self):
    calculator = SimpleCalculator()
    result = calculator.multiply(2, 6)
    self.assertEqual(result, 12)

  def test_divide(self):
    calculator = SimpleCalculator()


    result = calculator.divide(12, 3)
    self.assertEqual(result, 4)

    with self.assertRaises(ZeroDivisionError):
      calculator.divide(10, 0)

if __name__ == "__main__":
  unittest.main()