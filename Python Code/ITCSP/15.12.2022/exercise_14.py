## Enter a file name with its extension. Check if the extension is pdf type or not, and alert the result.
## Use input, string slicing and terniary operator

fileName = input("type your file name together with its extension ")
print("Your file is a pdf.") if (fileName[-3:] == "pdf") else print("Your file is not a pdf.")