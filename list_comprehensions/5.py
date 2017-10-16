

print [(x, y) for x in range(5) for y in range(x) if (x+y)%2 == 0]
