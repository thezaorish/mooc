#!/usr/bin/python

__author__ = 'training'

import sys

hitCount = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisCount = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", hitCount
        oldKey = thisKey
        hitCount = 0

    oldKey = thisKey
    hitCount += float(thisCount)

if oldKey != None:
    print oldKey, "\t", hitCount