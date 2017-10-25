

class Myclass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

print Myclass.i
print Myclass.f

a = Myclass()
print a.f()
