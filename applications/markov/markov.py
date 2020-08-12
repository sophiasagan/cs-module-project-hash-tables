import random
import os
import sys

# Read in all the words in one go
with open(os.path.join(sys.path[0], "input.txt")) as f:
    words = f.read()
    words = words.split()

f.close()

# TODO: analyze which words can follow other words
# Your code here
wonderland_dict = {}

for i in range(len(words) - 1):
    cur = words[i]
    next = words[i + 1]
    # If word is not in the dict
    if not cur in wonderland_dict.keys():
        wonderland_dict[cur] = [next]
    # If it is in the dict
    else:
        # append to the list
        wonderland_dict[cur].append(next)

# TODO: construct 5 random sentences
# Your code here

suffixes = ('.', '?', '!', '."', '?"', '!"')


def random_sentence(word):
    
    print(word, end=" ")
    # If it is a stop word, stop
    if word.endswith(suffixes):
        print('\n')
        return
    else:
        random_sentence(random.choice(wonderland_dict[word]))


random_sentence('Alice')
random_sentence('Do')
random_sentence('Kitty')
random_sentence('Red')
random_sentence('Now')
random_sentence('How')
random_sentence('In')
random_sentence('They')
random_sentence('King')
random_sentence('To')
random_sentence('Kitty')
random_sentence('Red')

