#!/usr/bin/python

# Input: forum_node.tsv
# format of each line:
# "id"	"title"	"tagnames"	"author_id"	"body"	"node_type"	"parent_id"	"abs_parent_id"	"added_at"	"score"	"state_string" "last_edited_id"
# "last_activity_by_id"	"last_activity_at"	"active_revision_id"	"extra"	"extra_ref_id"  "extra_count"	"marked"

# Output: tag   1

import sys
import re

NUMBER_OF_COLUMNS = 19
TAGS_INDEX = 2
NODE_TYPE_INDEX = 5

full_line = ''  # accumulates the full post entry from consecutive lines of text

for line in sys.stdin:
    if line.count('node_type', 0, len(line)) == 1:  # ignores the file header
        continue

    full_line += line
    data = full_line.strip().split("\t")

    if len(data) == NUMBER_OF_COLUMNS:  # the entire post has been read
        node_type = data[NODE_TYPE_INDEX]
        if node_type in ('question', '"question"'):
            tags = data[TAGS_INDEX].replace('"', '')

            for tag in re.split(' ', tags):  # the tags are just words
                tag = tag.strip()
                if tag != '':
                    print "{0}\t{1}".format(tag.lower(), 1)
        full_line = ''