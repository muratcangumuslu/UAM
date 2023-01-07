def swap_values(x, y):
  # Use a temporary variable to swap the values of x and y
  temp = x
  x = y
  y = temp

  # Print the new values of x and y using f-strings
  print(f"x = {x}")
  print(f"y = {y}")

# Test the function
swap_values(1, 2)
swap_values(3, 4)
swap_values(5, 6)