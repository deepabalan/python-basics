

def histogram(s):
    t = {}
    for c in s:
        t[c] = t.get(c, 0) + 1
    return t


def print_hist(h):
    for c in h:
        print c, h[c]


h = histogram('parrot')

print_hist(h)
