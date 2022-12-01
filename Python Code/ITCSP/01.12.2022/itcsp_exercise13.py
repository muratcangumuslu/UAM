# Enter 3 integers x, y, z, calculate and print the smallest number

firstN = int(input("Type the first number "))
secondN = int(input("Type the second number "))
thirdN = int(input("Type the third number "))

if firstN < secondN and firstN < thirdN:
    print(f"the smallest number is {firstN}")
elif secondN < firstN and secondN < thirdN:
    print(f"the smallest number is {secondN}")
elif thirdN < firstN and thirdN < secondN: 
    print(f"the smallest number is {thirdN}")