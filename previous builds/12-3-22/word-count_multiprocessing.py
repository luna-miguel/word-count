# Python word counter
# CSC 11300 - Programming language
# Miguel Luna

import re
from operator import *
import time
import multiprocessing

output = multiprocessing.Queue()

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
def count_words(word_list, output):
    words = list()
    frequencies = list()

    for current_word in word_list: 
        if current_word not in words:
            words.append(current_word)
            frequencies.append(1)
        else:
            frequencies[words.index(current_word)] += 1 # Increase frequency of known word

    result = list(zip(words, frequencies)) # Create tuples
    for count in result:
        output.put(count)   # Send tuples to queue

# Function to combine work done to split array of words from processes into total word counts
def aggregate(results):
    # unzipped = list(list(zip(*results))) Decouples the tuples
    unzipped_words = list(list(zip(*results))[0]) # Decouples the tuples, takes the words into a list
    unzipped_frequencies = list(list(zip(*results))[1]) # Decouples the tuples, takes the frequencies into a list

    zipped_words = list()
    zipped_frequencies = list()

    for i in range(len(unzipped_words)):
        if unzipped_words[i] not in zipped_words:
            zipped_words.append(unzipped_words[i])
            zipped_frequencies.append(unzipped_frequencies[i])
        else:
            zipped_frequencies[zipped_words.index(unzipped_words[i])] += unzipped_frequencies[i]

    return list(zip(zipped_words, zipped_frequencies))

if __name__ == "__main__":

    filepath = "/Users/miguelluna/Documents/GitHub/word-count/text files/test.txt"

    t = time.time()

    reader = open(filepath, 'r') 
    text = reader.read() # Read file in entirety
    reader.close()

    words_list = extract_words(text)
 
    split_list = slice_per(words_list, 8)

    p1 = multiprocessing.Process(target = count_words, args = (split_list[0], output, )) 
    p2 = multiprocessing.Process(target = count_words, args = (split_list[1], output, )) 
    p3 = multiprocessing.Process(target = count_words, args = (split_list[2], output, )) 
    p4 = multiprocessing.Process(target = count_words, args = (split_list[3], output, )) 
    p5 = multiprocessing.Process(target = count_words, args = (split_list[4], output, )) 
    p6 = multiprocessing.Process(target = count_words, args = (split_list[5], output, )) 
    p7 = multiprocessing.Process(target = count_words, args = (split_list[6], output, )) 
    p8 = multiprocessing.Process(target = count_words, args = (split_list[7], output, )) 
    processes = [p1, p2, p3, p4, p5, p6, p7, p8]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    results = []
    for p in processes:
        while output.empty() == False:
            results.append(output.get())

    total = aggregate(results)

    for frequency in total:
        print(frequency[0], "\t- ", frequency[1])

    print("Done. Time taken: {}".format(time.time() - t) + " seconds\n")
    
