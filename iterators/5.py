

import itertools

it1 = iter([1, 2, 3])
it2 = iter([4, 5, 6])
t = itertools.chain(it1, it2)
print t
