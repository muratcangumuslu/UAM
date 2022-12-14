## Write a program that counts vowels in a string, the program should implement the possibility of the user typing any word.

vowels = "aeiouAEIOU"
vowelCount = 0 # iterator
word = input("type your word ")
for ch in word :
    if ch in vowels:
        vowelCount += 1
print(f"You have {vowelCount} vowels in the word {word}")