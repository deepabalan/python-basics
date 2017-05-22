# Swapping values, cumbersome
a = 5
b = 3

print ('a = %d, b = %d') % (a, b)

temp = a
a = b
b = temp

print ('a = %d, b = %d') % (a, b)

# Swapping, more elegent
a = 2
b = 3
print ('a = %d, b = %d') % (a, b)
a, b = b, a
print ('a = %d, b = %d') % (a, b)

# ValueError
# Number of variables on the left and the number of values on the right have to be same
a, b = 1, 2, 3
print a, b
