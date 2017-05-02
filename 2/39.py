
import time
import dis

def fun1(filename):
    t = []
    f = open(filename)
    for word in f:
        s = word.strip()
        t = t + [s]
    return t

start = time.time()
fun1('wordslist.txt')
end = time.time() - start

print start, end

print dis.dis(fun1)
