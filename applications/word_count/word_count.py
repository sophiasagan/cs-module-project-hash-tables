def word_count(s):
    # Your code here
    word_d = {}

    remove = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'
    
    words = s.split()

    for word in words:
        word = word.strip(remove)
        word = "".join(i.lower() for i in word if not i in remove)

        if word == '': 
            continue

        if word not in word_d:
            word_d[word] = 0

        word_d[word] += 1

    return word_d


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))