

def reverse_lookup(d, v):
    for key in d:
        if d[key] == v:
            return key
    raise ValueError('Value does not appear in the dict()')
    # raise causes an exception called valueError

h = reverse_lookup({'a': 2, 'b': 8}, 2)
print h
