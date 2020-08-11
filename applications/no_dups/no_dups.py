no_dups_cache = {}

def no_dups(s):
    # Your code here
    for word in s:
        no_dups_cache[word] = True

    return s in no_dups_cache




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))