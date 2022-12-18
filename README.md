# word-count
Miguel Luna - Python word counter
CSC 113 - Programming Language Fall 2022

This program is designed to count the frequencies of words in a given text file.

Text files are located in the "text files" folder. When running the program, find the line containing the variable "filepath" in the main function and
modify it to hold the right filepath. For example, this is the line I use to use file "ttt.txt" from my GitHub folder in Documents:
```
filepath = "/Users/miguelluna/Documents/GitHub/word-count/text files/ttt.txt"
```

To modify the amount of processes if using the code that uses multiprocessing:
1. Change the parameter number in the function call of slice_per assigned to split_list
to the needed number of processes.
2. Add or remove all mentions processes p1, p2, etc. from the code and processes list.
For example, if we are using three processes, the modified code would look like:
```
    split_list = slice_per(words_list, 3)

    p1 = multiprocessing.Process(target = count_words, args = (split_list[0], output, ))
    p2 = multiprocessing.Process(target = count_words, args = (split_list[1], output, ))
    p3 = multiprocessing.Process(target = count_words, args = (split_list[2], output, )) 
    
    processes = [p1, p2, p3]
```
