# Python word counter
# CSC 11300 - Programming language
# Miguel Luna


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