# Write a function array to create an 2-dimensional array. The function
# should take both dimensions as arguments. Value of each element can be
# initialized to None:


def array(row, column):
    return [[None for x in range(column)] for x in range(row)]

a = array(2, 3)
print a

a[0][0] = 5
print a
