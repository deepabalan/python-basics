# If the global value is mutable, you can modify it without declaring
# it:


known = {0: 0, 1: 1}


def fun1():
    known[2] = 1
    print known


print known
fun1()
print known
