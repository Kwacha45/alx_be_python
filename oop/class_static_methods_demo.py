class Calculator:
  calculation_type = "Arithmetic Operations"  # Class attribute

  @staticmethod
  def add(a, b):
    return a + b

  @classmethod
  def multiply(cls, a, b):
    print(f"Performing {cls.calculation_type}:")
    return a * b

# Example usage
sum_result = Calculator.add(5, 3)
product_result = Calculator.multiply(4, 2)

print(f"Sum: {sum_result}")
print(f"Product: {product_result}")