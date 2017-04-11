# factorial

def factorial(n):
    print ' '*n, 'factorial', n
    if n == 0:
        print ' '*n,'returning 1'
        return 1
    else:
        result = n * factorial(n - 1)
        print ' '*n, 'returning', result
        return result

print factorial(5)
print factorial(10)
print factorial(0)
print factorial(3)
