#!/usr/bin/python

__author__ = 'training'

import sys

oldKey = None
totalCostPerDay = 0
purchasesPerDay = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the weekday, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        mean = totalCostPerDay / purchasesPerDay
        print oldKey, "\t", mean
        oldKey = thisKey
        totalCostPerDay = 0
        purchasesPerDay = 0

    oldKey = thisKey
    totalCostPerDay += float(thisSale)
    purchasesPerDay += 1

if oldKey != None:
    print oldKey, "\t", totalCostPerDay / purchasesPerDay