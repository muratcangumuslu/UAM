## Enter a file name with its extension, check if it is a pdf, if it is, print the result in a sentence eg. "Your file is a pdf"
## If it is not, print the file with its extension in a sentence eg. "Your file has a .doc extension"
## Print an error message if the user does not type an extension for the file

fileName = input("type your file name together with its extension ")
extension = fileName.split(".")

if "." not in fileName:
    print("You entered a file name without an extension")
elif fileName[-3:] == "pdf":
    print("Your file is a pdf.") 
elif fileName[-3:] != "pdf":
    print(f"Your file's extension is {extension[1]}.") 
