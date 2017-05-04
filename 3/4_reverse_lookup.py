

def reverse_lookup(d, v):
    t = []
    for key in d:
        if key not in t:
            if d[key] == v:
                t.append(key)
    return t, v

h = {'a': 3, 'b': 3, 'c': 8, 'd': 3}

print reverse_lookup(h, 3)
print reverse_lookup(h, 0)
