

def expo(x, n):
    if n == 0:
        return 1
    else:
        return x * expo(x, n-1)

print expo(2, 10)
print expo(3, 10)

