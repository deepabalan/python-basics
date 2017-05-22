
# A value in parenthesis is not a tuple
t = ('a')
print type(t)

# Create tuple
t = tuple()
print type(t)

# Create a tuple with single element
t = 'a',
print type(t)

# If the argument is a sequence, the result is a tuple with the elements of the sequence
t = tuple('deepa')
print t
