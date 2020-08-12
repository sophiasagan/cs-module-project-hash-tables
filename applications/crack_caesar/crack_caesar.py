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
    cipher = {}

    text = text.translate(str.maketrans(
        "", "", ' ":;,.-+=/\\|[]{}()*^&\n\'\!—?1'
        ))

    for word in text:
        if word in cipher:
            cipher[word] += 1
        else:
            cipher[word] = 1

    cipher_items = list(cipher.items())

    cipher_items.sort(key=lambda pair: pair[1], reverse=True)

    cipher_items = [x[0] for x in cipher_items]

    return cipher_items

decoder = dict(zip(crack_caesar(words), frequencies))

print(words.translate(str.maketrans(decoder)))
