# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import os
import sys

frequencies = (
    "E",
    "T",
    "A",
    "O",
    "H",
    "N",
    "R",
    "I",
    "S",
    "D",
    "L",
    "W",
    "U",
    "G",
    "F",
    "B",
    "M",
    "Y",
    "C",
    "P",
    "K",
    "V",
    "Q",
    "J",
    "X",
    "Z",
)

with open(os.path.join(sys.path[0], 'ciphertext.txt')) as f:
    words = f.read()
    # words = words.split()

# f.close()

# cipher = {}


def crack_caesar(text):
    # init dict
    cipher = {}
    # return a copy of the string without non-alphabetical char
    text = text.translate(str.maketrans(
        "", "", ' ":;,.-+=\\|[]{}()*^&\n\'\!—?1'
        ))
    # print(text)

    # iterate and count letters in cipher
    for word in text:
        if word in cipher:
            cipher[word] += 1
        else:
            cipher[word] = 1

    # convert dict to tuple
    cipher_items = list(cipher.items())
    # print(cipher_items)

    # sort the list by frequency
    cipher_items.sort(key=lambda pair: pair[1], reverse=True)
    # print(cipher_items)

    # map cipher letter to decoded letter
    cipher_items = [x[0] for x in cipher_items]
    # print(cipher_items)

    return cipher_items

# join tuples together return as dict
decoder = dict(zip(crack_caesar(words), frequencies))
# print items with non-alphabetical char 
print(words.translate(str.maketrans(decoder)))


