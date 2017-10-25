
import sys


def file_word(filename):
    f = open(filename).read().split()
    count = {}
    for x in f:
        count[x] = count.get(x, 0) + 1
    for k, v in count.items():
        print k, '\t', v

file_word(sys.argv[1])

#if __name__ == "__file_word__":
#    import sys
#    file_word(sys.argv[1])
