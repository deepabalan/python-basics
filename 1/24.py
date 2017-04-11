# Factorial modification


def fact(n):
    if not isinstance(n, int):
        print 'Factorial is defined only for integers.'
        return None
    elif n < 0:
        print 'Factorial is not defined for negative numbers.'
        return None
    elif n == 0:
        return 1
    else:
        return n * fact(n-1)


print fact(5.9)
print fact(-9)
print fact(8)
print fact('deepa')
