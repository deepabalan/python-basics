# Python provides a built-in function filter(f, a) that returns items
# of the list a for which f(item) returns true. Provide an
# implementation for filter using list comprehensions.


def even(x): return (x % 2) == 0


def filter_list(f, v):
    return [x for x in v if f(x)]

print filter_list(even, range(10))
