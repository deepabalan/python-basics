# comparing tuples
# python starts by comparing the first element from each sequence.
# If they are equal, it goes on to next elements, and so on, until it
# finds elements that differ. Subsequent elements are not considered (
# even if they are really big.

print (0, 1, 2) < (0, 3, 4)

print (0, 1, 200000) < (0, 3, 4)

print (2, 1, 2) > (4, 0, 0)
