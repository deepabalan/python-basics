# print a string n times


def print_s(s, n):
    if n > 0:
        print s
        print_s(s, n-1)
    else:
        return
print_s('deepa', 2)
