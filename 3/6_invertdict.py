

def invert_dict(d):
    inverse = {}
    for key in d:
        value = d[key]
        if value not in inverse:
            inverse[value] = [key]
        else:
            inverse[value].append(key)
    return inverse

h = {'a': 1, 'p': 2, 'l': 1, 'e': 1}

print invert_dict(h)
