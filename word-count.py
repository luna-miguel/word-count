# Python word counter
# CSC 11300 - Programming language
# Miguel Luna

import re

# Class that holds a given word and the frequency of that word in a text.
class WordFrequency:    

    def __init__(self, word, frequency = 1): # constructor
        if type(word) != str:
           raise ValueError("Word must be of a string type.") 
        self.word = word
        if frequency == 0:
            raise ValueError("Frequency of a new word cannot be zero.")
        self.frequency = frequency

    def __str__(self): # string overloading function
        return self.word

def extract_words(filepath):

    reader = open(filepath, 'r') 
    text = reader.read() # read file in entirety
    reader.close()

    word_list = re.split(r"[\b\W\b]+", text) # delimiter = all non-alphanumeric characters
    
    for i in range(len(word_list)): # put all words into lowercase
        word_list[i] = word_list[i].lower()
        
    return word_list

# Filepath of text on my desktop: extract_words(r"/Users/miguelluna/Desktop/sample.txt")

# sample.txt:   ThiS-Is!A       SAmPLE senTEnce.
#               IF doNe$CORRectLY, THIs+wILl*onLY&takE
#               tHE@woRDs#, aLL^iN%loWErcaSe.

# Output of each element of the list produced by extract_words:

# this
# is
# a
# sample
# sentence
# if
# done
# correctly
# this
# will
# only
# take
# the
# words
# all
# in
# lowercase