# Provide an implementation for zip function using list comprehensions.


def zip_list(a, b):
    if len(a) > len(b):
        return [(a[i], b[i]) for i in range(len(b))]
    else:
        return [(a[i], b[i]) for i in range(len(a))]

print zip_list([1, 2, 3], ["a", "b", "c"])
