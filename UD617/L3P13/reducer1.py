#!/usr/bin/python

__author__ = 'training'

import sys

salesCount = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    salesCount += float(thisSale)

print salesCount