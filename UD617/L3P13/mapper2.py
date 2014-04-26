#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want total values of sales
# We need to write them out to standard output, separated by a tab

__author__ = 'training'

import sys

cnt = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        cnt += float(cost)
print "{0}\t{1}".format("1", cnt)