# invert_dict using setdefault


def invert_dict(d):
    t = {}
    for key in d:
        value = d[key]
        t.setdefault(value, []).append(key)
    return t


h = {'a': 2, 'b': 3, 'c': 3}

print invert_dict(h)
