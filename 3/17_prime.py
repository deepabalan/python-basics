# checking prime number

import random


def prime_check(n):
    if n % 2  != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
        print 'prime number'
    else:
        print 'Not prime number'

a = random.randint(1, 100)

print a
prime_check(a)
