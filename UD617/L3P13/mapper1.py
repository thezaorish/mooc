#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want number of sales
# We need to write them out to standard output, separated by a tab

__author__ = 'training'

import sys

cnt = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        cnt += 1
print "{0}\t{1}".format("1", cnt)