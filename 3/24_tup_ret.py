# Tuples as return values
# Inefficient method

x = 15
y = 3

def fun():
    return x / y, x % y

print fun()

# Another way to use built-in function 'divmod'
t = divmod(7, 3)
print t

quo, rem = divmod(17, 4)
print quo
print rem
