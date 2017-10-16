

tup = [('aa', 8), ('a', 15), ('w', 2)]

def fun(s):
    return s[1]

d = sorted(tup, key=fun, reverse=True)
print d
