
import sys


def cat_py(filenames):
    f = open(filenames)
    print f.read()

cat_py(sys.argv[1])
