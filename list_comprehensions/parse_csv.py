# Write a python function parse_csv to parse csv files.

import sys


def parse_csv(filename):
    return [line.strip().split(',') for line in open(filename).readlines()]

print parse_csv(sys.argv[1])
