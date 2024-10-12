import math

class Shape:
  def area(self):
    raise NotImplementedError("Area calculation not implemented for base Shape class.")

class Rectangle(Shape):
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return math.pi * self.radius**2

# Example usage
rectangle = Rectangle(5, 3)
circle = Circle(4)

print(f"Rectangle area: {rectangle.area()}")
print(f"Circle area: {circle.area():.2f}")  # Format circle area with 2 decimal places