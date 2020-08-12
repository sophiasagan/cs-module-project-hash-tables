# Your code here
import os
import sys

with open(os.path.join(sys.path[0], 'robin.txt')) as f:
    words = f.read()
    # words = words.split()

f.close()

ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'

# histo_cache = {}

def histo(file):
    histo_cache = {} # init dict

    words_list = words.split() # split words

    for word in words_list:
        word = word.lower().strip(ignore) # lowercase and remove non alphabetic

        if word not in histo_cache: # check dict for word
            if word == "":
                continue # if not word, skip
            histo_cache[word] = "" # add word to cache

        histo_cache[word] += "#" # increment

    # Sort the tuples
    histo_items = list(histo_cache.items())
    # reverse list so that greatest it at top & alphabetize
    histo_items.sort(key = lambda pair: (-len(pair[1]), pair[0]))

    for item in histo_items:
        print(f"{item[0] :20}{item[1]}") # justify items
