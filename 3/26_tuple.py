# Variable-length argument tuples

# A parameter name that begins with * gathers arguments into a tuple.
def printall(*args):
    print args


printall(1, 2.0, '3')
