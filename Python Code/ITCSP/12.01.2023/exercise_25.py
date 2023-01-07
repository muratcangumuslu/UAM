# Get the values of x and y from the user
x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))

# Use a temporary variable to swap the values of x and y
temp = x
x = y
y = temp

# Print the new values of x and y
print("x =", x)
print("y =", y)