# Python word counter
# CSC 11300 - Programming language
# Miguel Luna

import re
from operator import *
import time

# Function to extract each word from the given text, using regular expressions.
def extract_words(text):

    word_list = re.split(r"[\b\W\b]+", text) # Delimiter = all non-alphanumeric characters
    # [] matches everything contained within
    # \b matches a word boundary (start OR end of a word string)
    # \W matches all characters that are not alphanumeric
    # + matches all instances of preceding tokens (the token being [\b\W\b])
    
    for i in range(len(word_list)): # Put all words into lowercase
        word_list[i] = word_list[i].lower()
        
    return word_list
    
# Function to slice the text into steps for separate processes to handle individually
def slice_per(source, step): 
    return [source[i::step] for i in range(step)]
      
# Function to count the frequencies of each word.
def count_words(word_list):
    words = list()
    frequencies = list()

    for current_word in word_list: 
        if current_word not in words:
            words.append(current_word) # insert the word into known words if new word found
            frequencies.append(1) 
        else:
            frequencies[words.index(current_word)] += 1 # update the word count if known word found

    return list(zip(words, frequencies)) # combine words and frequencies into tuples

filepath = "/Users/miguelluna/Documents/GitHub/word-count/text files/ttt.txt"

t = time.time()

reader = open(filepath, 'r') 
text = reader.read() # Read file in entirety
reader.close()

words_list = extract_words(text)
results = count_words(words_list)

for frequency in results:
    print(frequency[0], "\t- ", frequency[1])

print("Done. Time taken: {}".format(time.time() - t) + " seconds\n")




