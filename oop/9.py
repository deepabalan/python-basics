

class Dog:

    tricks = []             # mistaken use of class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Figo')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print d.tricks              # unexpectadly shared by all dogs
