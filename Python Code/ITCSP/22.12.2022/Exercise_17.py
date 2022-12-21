## write a program that will reverse the order of a string and print it to the console
## the program should continue to ask for a string to reverse until the user types "exit" as input

myStr = ""
while myStr != "exit":
    myStr = input("Type your string ")
    if myStr == "exit":
        break
    else:
        reversedStr = myStr[::-1]
        print(reversedStr)