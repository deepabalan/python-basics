# Python provides a built-in function map that applies a function to
# each element of a list. Provide an implementation for map using list
# comprehensions.


def square(x): return x * x


def map_list(f, v):
    return [f(i) for i in v]

print map_list(square, range(5))
