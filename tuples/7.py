# swapping

a = 5
b = 3

print 'before swapping... a = %d, b = %d' % (a, b)

temp = a
a = b
b = temp

print 'after swapping... a = %d, b = %d' % (a, b)

# swapping using tuple

a = 5
b = 3
a, b = b, a

print a, b
