#!/usr/bin/python

# Format of each line:
# "id"	"title"	"tagnames"	"author_id"	"body"	"node_type"	"parent_id"	"abs_parent_id"	"added_at"	"score"	"state_string"
#   "last_edited_id"	"last_activity_by_id"	"last_activity_at"	"active_revision_id"	"extra"	"extra_ref_id"
#   "extra_count"	"marked"

# We want to extract all words from the body of the forum post

__author__ = 'training'

import sys
import re

full_line = ""
for line in sys.stdin:
    if line.count("node_type", 0, len(line)) == 1:
        continue

    full_line += line
    data = full_line.strip().split("\t")
    if len(data) == 19:
        for term in re.split('\.|!|\?|:|;|\"|\(|\)|<|>|\[|\]|#|$|=|-|/| |,', data[4]):
            term = term.strip()
            if term != '':
                print "{0}\t{1}".format(term.strip().lower(), data[0])
        full_line = ""