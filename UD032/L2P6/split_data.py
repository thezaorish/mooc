#!/usr/bin/env python
# -*- coding: utf-8 -*-
# So, the problem is that the gigantic file is actually not a valid XML, because
# it has several root elements, and XML declarations.
# It is, a matter of fact, a collection of a lot of concatenated XML documents.
# So, one solution would be to split the file into separate documents,
# so that you can process the resulting files as valid XML documents.

__author__ = 'zaorish'

import xml.etree.ElementTree as ET
PATENTS = 'patent.data'

def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def split_file(filename):
    counter = 0
    file_content = ''
    with open(filename, "r") as f:
        for line in f:
            if (line.startswith('<?xml version')) & (len(file_content) > 0):
                new = open(filename + '-' + str(counter), 'w')
                new.write(file_content)
                file_content = ''
                counter += 1
            file_content += line

        new = open(filename + '-' + str(counter), 'w')
        new.write(file_content)


def test():
    split_file(PATENTS)
    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print "You have not split the file {} in the correct boundary!".format(fname)
            f.close()
        except:
            print "Could not find file {}. Check if the filename is correct!".format(fname)


test()
