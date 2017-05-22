# Most list operators work on tuples.

# Bracket operator
t = (1, 2, 3, 4, 5)
print t[-1]

# Slice operator
print t[:]
print t[::-1]

# Modification: Fails, tuples: Immutable
# t[0] = 'one'
# print t

# Replacement: possible
t = ('one',) + t[1:]
print t
