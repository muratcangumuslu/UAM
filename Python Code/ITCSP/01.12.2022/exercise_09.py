# Write a program that asks the user for their first name, birth year and the current year, and then calculates their age.
# Print the result in the console as "Xyz, you are 12 years old."
# Use "new line" \n

firstName = input("Type your name \n")
birthYear = input("Type your birth year \n")
currentYear = input("Type the current year \n")

age = (int(currentYear) - int(birthYear))
myStr = f"{firstName}, you are {age} years old."
print(myStr)