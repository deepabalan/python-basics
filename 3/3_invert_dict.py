

def invert_dict(d):
    inverse = {}
    for key in d:
        value = d[key]
        if value not in inverse:
            inverse[value] = [key]
        else:
            inverse[value].append(key)
    return inverse


h = {'a': 1, 'e': 2, 'p': 1, 'd': 1}

print invert_dict(h)
