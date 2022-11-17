# Write a program that calculates a "delta" for the quadratic equation as below
# y = 3x2 - 4x + 1

# The formula for the delta is as following;
# y = ax2 + bx + c
# delta = b2 - 4ac

a = 3
b = 4
c = 1

delta = (b ** 2) - (4 * a * c)
print("Delta equals: " + str(delta))