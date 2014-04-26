#!/usr/bin/python

__author__ = 'training'

import sys

nodes = []
oldterm = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    term, nodeId = data_mapped

    if oldterm and oldterm.lower() != term.lower():
        print oldterm, "\t", nodes
        oldterm = term
        nodes = []

    oldterm = term
    nodes.append(nodeId)

if oldterm != None:
    print oldterm, "\t", nodes