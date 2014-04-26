#!/usr/bin/python

__author__ = 'training'

import sys

occurrencesTotal = 0
oldterm = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    term, nodeId = data_mapped

    if oldterm and oldterm.lower() != term.lower():
        print oldterm, "\t", occurrencesTotal
        oldterm = term
        occurrencesTotal = 0

    oldterm = term
    occurrencesTotal += 1

if oldterm != None:
    print oldterm, "\t", occurrencesTotal