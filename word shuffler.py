import random

word = input("Enter a word: ")

# Convert the word to a list of characters
letters = list(word)

# Shuffle the list of letters
random.shuffle(letters)

# Convert the shuffled list back to a string
shuffled_word = ''.join(letters)

print("Shuffled word:", shuffled_word)
