
def no_dups(s):
    # Your code here
    s = s.split() # split string
    s = list(dict.fromkeys(s)) # create list with dict keys - removes dups
    s = ' '.join(s) # join list with space between words
    return s






if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
