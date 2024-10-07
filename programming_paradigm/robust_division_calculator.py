def safe_divide(numerator, denominator):

  try:
    numerator = float(numerator)
    denominator = float(denominator)

    result = numerator / denominator
    return f"Result: {result:.2f}"

  except ZeroDivisionError:
    return "Error: Cannot divide by zero."
  except ValueError:
    return "Error: Invalid input. Please enter numbers only."