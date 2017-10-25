
import os
import sys


def tree(name):
    for root, dirs, files in os.walk(name):
        print root,
        print dirs,
        print files
tree(sys.argv[1])
