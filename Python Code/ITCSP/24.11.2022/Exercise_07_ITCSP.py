# Create a string made of the first, middle and last character and print it to the terminal

str1 = input("Type your string ") # gets user input
firstChr = str1[0] 
lastChr = str1[-1]
middleChrIndex = int(len(str1)/2) # when the string length is even, dividin it by 2 gives back a float which cannot be used as an index, hence the int fucntion
# print(type(middleChrIndex)) - to check the type

middleChr = str1[middleChrIndex]
result = firstChr + middleChr + lastChr
print(result)
