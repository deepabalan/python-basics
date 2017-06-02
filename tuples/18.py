# dictionaries and tuples


d = {'a': 0, 'b': 1, 'c': 2}
t = d.items()
print t, type(t)

# the other way round


t = [('a', 0), ('b', 1), ('c', 2)]
d = dict(t)
print d, type(d)
