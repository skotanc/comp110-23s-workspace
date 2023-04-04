"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730551547"
word: str = input("Enter a 5-character word: ")
if (len(word) != 5):
    print("Error: Word must contain 5 characters")
    exit()
letter: str = input("Enter a single character: ")
if (len(letter) != 1):
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + letter + " in " + word)
match = 0
if (word[0] == letter):
    print(letter + " found at index 0")
    match = match + 1
if (word[1] == letter):
    print(letter + " found at index 1")
    match = match + 1
if (word[2] == letter):
    print(letter + " found at index 2")
    match = match + 1
if (word[3] == letter):
    print(letter + " found at index 3")
    match = match + 1
if (word[4] == letter):
    print(letter + " found at index 4")
    match = match + 1
if (match == 0):
    print("No instances of " + letter + " found in " + word)
if (match == 1):
    print(str(match) + " instance of " + letter + " found in " + word)
if (match > 1):
    print(str(match) + " instances of " + letter + " found in " + word)
