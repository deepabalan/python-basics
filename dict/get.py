

a = {'x': 10, 'y': 2, 'z': 3}

print a.get('x', 5)
print a.get('p', 9)

print a.setdefault('x', 0)
print a

print a.setdefault('p', 0)
print a

print a.get('y')
