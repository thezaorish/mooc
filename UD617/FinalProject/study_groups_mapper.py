#!/usr/bin/python

# Input: forum_node.tsv
# format of each line:
# "id"	"title"	"tagnames"	"author_id"	"body"	"node_type"	"parent_id"	"abs_parent_id"	"added_at"	"score"	"state_string" "last_edited_id"
# "last_activity_by_id"	"last_activity_at"	"active_revision_id"	"extra"	"extra_ref_id"  "extra_count"	"marked"

# Output: question id    user id
# question id = the node if the post = question
#             = the absolute parent node id if post = answer or comment

import sys

NUMBER_OF_COLUMNS = 19
ID_INDEX = 0
AUTHOR_INDEX = 3
NODE_TYPE_INDEX = 5
ABS_PARENT_ID_INDEX = 7

full_line = ''  # accumulates the full post entry from consecutive lines of text

for line in sys.stdin:
    if line.count('node_type', 0, len(line)) == 1:  # ignores the file header
        continue

    full_line += line
    data = full_line.strip().split("\t")

    if len(data) == NUMBER_OF_COLUMNS:  # the entire post has been read
        node_type = data[NODE_TYPE_INDEX]

        author_id = data[AUTHOR_INDEX]
        if node_type in ('question', '"question"'):
            post_id = data[ID_INDEX]
        else:
            post_id = data[ABS_PARENT_ID_INDEX]

        print "{0}\t{1}".format(post_id, author_id)

        full_line = ''