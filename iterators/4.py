# Write an iterator class reverse_iter, that takes a list and iterates
# it from the reverse direction.


class reverse_iter:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

rev = reverse_iter([1, 2, 3, 4])
for i in rev:
    print i
