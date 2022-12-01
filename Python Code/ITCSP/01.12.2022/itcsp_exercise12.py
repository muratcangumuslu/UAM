# if the number is divisible by 2 and 3 print "divisible by 2 and 3"
# if the number is divisible by 2 and not by 3 print ...
# if the number is divisible by 3 and not by 2 print ...
# if the number is nit divisible either by 2 and 3 print ...

myNumber = int(input("Type your number "))

if (myNumber % 2 == 0) and (myNumber % 3 == 0):
    print("the number is divisible by both 2 and 3")
elif (myNumber % 2 == 0) and (myNumber % 3 != 0):
    print("the number is divisible by 2 but not by 3")
elif (myNumber % 2 != 0) and (myNumber % 3 == 0):
    print("the number is divisible by 3 but not by 2")
elif (myNumber % 2 != 0) and (myNumber % 3 != 0):
    print("the number is not divisible neither by 3 nor by 2")