# Author: Caleb Moura

# Prompt user to input 5 unique words
word1 = input("Enter the first unique word: ")
word2 = input("Enter the second unique word: ")
word3 = input("Enter the third unique word: ")
word4 = input("Enter the fourth unique word: ")
word5 = input("Enter the fifth unique word: ")

# List of the input values in the order given by the user
words_list = [word1, word2, word3, word4, word5]

# List display where each index corresponds to length of the word at corresponding index
lengths_list = [len(word) for word in words_list]
print("List of word lengths:", lengths_list)

# I got lost on the last part so I looked at a "python for dummies" vid to guide me a bit with tags