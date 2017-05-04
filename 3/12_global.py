

state = True


def fun1():
    global state
    state = False
    print 'inside fun1() ...', state

fun1()

print 'outside fun1() ...', state

fun1()
