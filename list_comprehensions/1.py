

a = range(10)
print a

print [x for x in a]

print [x for x in a if x % 2 == 0]

print [x * x for x in a if x % 2 == 0]

print [x + 1 for x in a]
