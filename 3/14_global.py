

count = 0


def fun1():
    global count
    count += 1
    print count

print count
fun1()
print count
