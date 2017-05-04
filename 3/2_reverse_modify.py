

def reverse_lookup(d, v):
    a = []
    for i in d:
        if i not in a:
            if d[i] == v:
                a.append(i)
    return (a, v)

d = {'a': 1, 'b': 1, 'c': 1, 'd': 2}
print reverse_lookup(d, 1)
