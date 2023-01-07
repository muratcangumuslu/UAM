def reverse_string(string):
  # Create an empty list to store the reversed string
  reversed_string = []

  # Iterate through the string in reverse order
  for i in range(len(string)-1, -1, -1):
    reversed_string.append(string[i])

  # Join the list of characters into a single string and return it
  return ''.join(reversed_string)

while True:
  string = input("Enter a string (or 'exit' to quit): ")
  if string == "exit":
    break
  reversed_string = reverse_string(string)
  print(reversed_string)