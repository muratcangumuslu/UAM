# Write a program that asks the user for their first name, birth year and the current year, and then calculates their age.
# Print the result in the console as "Xyz, you are 12 years old."

firstName = input("Type your name ")
birthYear = input("Type your birth year ")
currentYear = input("Type the current year ")

age = (int(currentYear) - int(birthYear))
myStr = f"{firstName}, you are {age} years old."
print(myStr)
