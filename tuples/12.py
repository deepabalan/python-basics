# variable-length argument tuples

# gather
def print_all(*args):
    print args

print_all(1, 2, 3, 3.5)


# scatter
t = (7, 3)

print divmod(*t)
