

import time

wordlist = ['a', 'b', 'c', 'd', 'e', 'f']


def fun():
    for i in wordlist:
        if i == 'd':
            return True
    return False

start_time = time.time()
t = fun()
elapsed_time = time.time() - start_time

print start_time, elapsed_time
