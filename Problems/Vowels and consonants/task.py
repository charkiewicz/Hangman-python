vowels = "aeiou"
consonants = "bcdfghjklmnpqrstuvwxyz"
word = str(input())

for character in word:
    if character in vowels:
        print("vowel")
        continue
    if character in consonants:
        print("consonant")
        continue
    break

