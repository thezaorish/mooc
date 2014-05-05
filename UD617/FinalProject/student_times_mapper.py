#!/usr/bin/python

# Input: forum_node.tsv
# format of each line:
# "id"	"title"	"tagnames"	"author_id"	"body"	"node_type"	"parent_id"	"abs_parent_id"	"added_at"	"score"	"state_string" "last_edited_id"
# "last_activity_by_id"	"last_activity_at"	"active_revision_id"	"extra"	"extra_ref_id"  "extra_count"	"marked"

# Output: student id    time of post
# Desired: extract the post author id (author_id column) and the date of the post (date_added column) for every entry in the input file

import sys
import re

NUMBER_OF_COLUMNS = 19
AUTHOR_ID_INDEX = 3
DATE_ADDED_INDEX = 8

full_line = ''  # accumulates the full post entry from consecutive lines of text

for line in sys.stdin:
    if line.count('node_type', 0, len(line)) == 1:  # ignores the file header
        continue

    full_line += line
    data = full_line.strip().split("\t")

    if len(data) == NUMBER_OF_COLUMNS:
        created = data[DATE_ADDED_INDEX]  # extract the date from the full line
        # "2014-01-14 17:18:35.613939+00"
        time = re.split(' ', created)[1]
        hour = re.split(':', time)[0]

        author_id = data[AUTHOR_ID_INDEX].strip("'").strip('"').strip()

        print "{0}\t{1}".format(author_id, int(hour))
        full_line = ''