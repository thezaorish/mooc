#!/usr/bin/python

# Input: forum_node.tsv
# format of each line:
# "id"	"title"	"tagnames"	"author_id"	"body"	"node_type"	"parent_id"	"abs_parent_id"	"added_at"	"score"	"state_string" "last_edited_id"
# "last_activity_by_id"	"last_activity_at"	"active_revision_id"	"extra"	"extra_ref_id"  "extra_count"	"marked"

# Output: forum id    classifier    length
# forum id = the node id, if post = question
#          = the parent node id, if post = answer

import sys

NUMBER_OF_COLUMNS = 19
ID_INDEX = 0
BODY_INDEX = 4
NODE_TYPE_INDEX = 5
PARENT_ID_INDEX = 6

full_line = ''  # accumulates the full post entry from consecutive lines of text

for line in sys.stdin:
    if line.count('node_type', 0, len(line)) == 1:  # ignores the file header
        continue

    full_line += line
    data = full_line.strip().split("\t")

    if len(data) == NUMBER_OF_COLUMNS:  # the entire post has been read
        node_type = data[NODE_TYPE_INDEX]
        if node_type in ('question', 'answer', '"question"', '"answer"'):
            post_id = data[ID_INDEX]
            parent_id = data[PARENT_ID_INDEX]
            # removing the double quotes around the body + getting rid of the double double quotes
            body = data[BODY_INDEX].lstrip('"').rstrip('"').strip().replace('""', '"')

            post_length = len(body)

            if node_type in ('question', '"question"'):   # classifier A is used to mark a question node
                print "{0}\t{1}\t{2}".format(post_id, 'A', post_length)
            else:   # classifier B is used to mark an answer node
                print "{0}\t{1}\t{2}".format(parent_id, 'B', post_length)

        full_line = ''