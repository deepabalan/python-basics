

def histogram(s):
    t = {}
    for c in s:
        if c not in t:
            t[c] = 1
        else:
            t[c] += 1
    return t


a = histogram('deepa')
print a

b = histogram('brontosaurus')
print b
