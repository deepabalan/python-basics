
# tuple: sequence of values
t = 'a', 'b', 'c'

print t,

print type(t)

t1 = ('d', 'e', 'f')

print t1,

print type(t1)

# tuples are indexed by integers
print t[0], t1[-1]

# tuples are immutable
t[0] = 'w'

print t

t3 = [1, 2, 3]

print t3

t3[0] = 2

print t3
