def word_count(s):
    # Your code here
    # init cache/dict
    word_d = {}
    # remove nonalphabetic chars
    remove = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'
    
    # split words into list
    words = s.split()

    # iterate through the list of words
    for word in words:
        # strip invalid chars, lowercase all letters
        # word = word.strip(remove)
        word = "".join(i.lower() for i in word if not i in remove)
        # check if word is valid
        if word == '': 
            continue
        # check dict for word
        if word not in word_d:
            word_d[word] = 0
        # add to word count
        word_d[word] += 1

    return word_d


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))