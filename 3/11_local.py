# local Vs global


been_called = True


def fun():
    been_called = False
    print 'inside fun() ...', been_called

print 'outside fun() ...', been_called

fun()
