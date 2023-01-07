def count_vowels(word):
  vowels = "aeiouAEIOU"
  vowel_count = 0 # iterator

  for ch in word:
      if ch in vowels:
          vowel_count += 1

  return f"You have {vowel_count} vowels in the word {word}"

# Test the function
print(count_vowels("hello"))
print(count_vowels("world"))
print(count_vowels("aeiou"))