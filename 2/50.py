# lookup

def lookup(d, k):
    for v in d:
        v = d[k]
    print v

h = lookup({'a': 1, 'b': 2, 'c': 3}, 'b')
