# isinstance() function

# myNumber = 5
# if isinstance(myNumber, int):
#     print("yes")
# else:
#     print("no")

# terniary operator, one line if else statements

# number = 5
# print("yes") if isinstance(number, int) else print("no")



# ---String Methods---

# 1. lower(), it returns a new value
myStr = "HOLA"
myLowerStr = myStr.lower()
print(myLowerStr)

# 2. upper(), returns a new value
myStr1 = "hello"
myUpperStr = myStr1.upper()
print(myUpperStr)

# 3. capitalize(), returns a new value
myStr2 = "hallo"
myCapStr = myStr2.capitalize()
print(myCapStr)

# 4. title(), returns a new value
myStr3 = "our first chapter"
myTitleStr = myStr3.title()
print(myTitleStr)

# 5. strip(), returns a new value
myStr4 = "       he lives in Poznan."
print(myStr4.strip())

# 6. strip(x), with parameter, returns a new value
myStr5 = "nhe live in Poznan"
print(myStr5.strip("n"))

# 7. strip(x), a longer string as parameter, returns a new value
myStr6 = "he lives in Poznan"
myStripStr = myStr6.strip("nhap")
print(myStripStr)

# 8. lstrip(x), returns a new value
myStr7 = "he lives in Poznan"
print(myStr7.lstrip("nha"))

# 9. find(value), it returns the index
myStr8 = "he lives somewhere"
print(myStr8.find('l'))

# 10 index(value), returns the index
myStr9 = "he lives in Warsaw"
print(myStr9.index("W"))

# 11 replace(old value, new value, new value number)
myStr10 = "he lives in Gdansk"
print(myStr10.replace("i", "a"))




# ---Iteration with while loop---

counter = 0
while counter < 6:
    print(counter)
    counter +=1


# --- Iteration with for loop ---

x = range(5)
for i in x:
    print(i)

for i in range(3, 20, 2): #adds 2, the last arguement
    print(i)


# Summarize all numbers from 0 to 3

mySum = 0 # initialize a variable
for i in range (0, 3):
    mySum += i
print("The sum of numbers is", mySum)


# Counting vowels in a string
vowels = "aeiou"
vowelCount = 0 # iterator
word = "appalachicola"
for ch in word :
    if ch in vowels:
        vowelCount += 1
print("number of vowels is", vowelCount)