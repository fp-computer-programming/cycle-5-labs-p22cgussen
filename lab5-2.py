# Author CCG AMDG 10/27/21

word1 = input("Enter a word: ")
word2 = input("Enter another word: ")

if word1 > word2:
    print(word1 + " comes after " + word2)
elif word1 < word2:
    print(word1 + " comes before " + word2)
else:
    print(" The words are the same")
