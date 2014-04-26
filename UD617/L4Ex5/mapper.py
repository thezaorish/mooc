#!/usr/bin/python

__author__ = 'training'

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 0 (turned into a weekday) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
from datetime import datetime

oldKey = None
totalCostPerDay = 0
purchasesPerDay = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()  # 0 to 6

        if oldKey != None and oldKey != weekday:
            mean = totalCostPerDay / purchasesPerDay
            print "{0}\t{1}".format(oldKey, mean)
            oldKey = weekday
            totalCostPerDay = 0
            purchasesPerDay = 0

        oldKey = weekday
        totalCostPerDay += float(cost)
        purchasesPerDay += 1

if oldKey != None:
    mean = totalCostPerDay / purchasesPerDay
    print "{0}\t{1}".format(oldKey, mean)