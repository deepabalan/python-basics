

def count(filename):
    return len(open(filename).read())
    
print count('foo.txt')
