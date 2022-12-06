# Python word counter
# CSC 11300 - Programming language
# Miguel Luna

import re
from operator import *
import time

# Class that holds a given word and the frequency of that word in a text.
class WordFrequency:    

    def __init__(self, word, frequency = 1): # Constructor
        if type(word) != str:
           raise ValueError("Word must be of a string type.") 
        self.word = word
        if frequency == 0:
            raise ValueError("Frequency of a new word cannot be zero.")
        self.frequency = frequency

    def __str__(self): # String overloading function
        return self.word

# Function to extract each word from the given text, using regular expressions.
def extract_words(filepath):

    reader = open(filepath, 'r') 
    text = reader.read() # Read file in entirety
    reader.close()

    word_list = re.split(r"[\b\W\b]+", text) # Delimiter = all non-alphanumeric characters
    # [] matches everything contained within
    # \b matches a word boundary (start OR end of a word string)
    # \W matches all characters that are not alphanumeric
    # + matches all instances of preceding tokens (the token being [\b\W\b])
    
    for i in range(len(word_list)): # Put all words into lowercase
        word_list[i] = word_list[i].lower()
        
    return word_list

# Function to count the frequencies of each word.
def count_words(word_list):
    remaining_words = word_list # Copy of word list to remove words as they are counted
    word_count = set() # Result list

    while len(remaining_words) > 0: 
        
        current_word = remaining_words[0] # Get the first word of the remaining list
        current_frequency = countOf(word_list, current_word) # Count the frequency
        new_word = WordFrequency(current_word, current_frequency)
        word_count.add(new_word)

        for i in range(current_frequency): # Remove all duplicates of the word in the list after counting it
            remaining_words.remove(current_word)

    return word_count

filepath = "/Users/miguelluna/Documents/GitHub/word-count/text files/test.txt"

t = time.time()

words_list = extract_words(filepath)
results = count_words(words_list)

for count in results:
    print(count.word, "\t- ", count.frequency)

print("Done. Time taken: {}".format(time.time() - t) + " seconds\n")