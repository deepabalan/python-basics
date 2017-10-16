# Generalize the above implementation of csv parser to support any
# delimiter and comments.

import sys


def parser(filename, delimiter, comment):
    return [line.strip().split(delimiter) for line in open(filename).readlines() if line[0] != comment]

print parser(sys.argv[1], '!', '#')
