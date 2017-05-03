

def read_words(filename):
    t = {}
    f = open(filename)
    for word in f:
        s = word.strip()
        t[s] = None
    return t

a = read_words('wordslist.txt')
print a
print 'expands' in a
