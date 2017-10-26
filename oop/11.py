# function defined outside the class

def f1(self, x, y):
    return min(x, x + y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

s = C()
print s.f(2, 3)
print s.g()
print s.h()
print s.__class__
