

def yrange(x):
    i = 0
    while i < x:
        yield i
        i += 1

y = yrange(3)
print y.next()
print y.next()
print y.next()
print y.next()
