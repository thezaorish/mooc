#!/usr/bin/python

# a line in the forum data
# "id"	"title"	"tagnames"	"author_id"	"body"	"node_type"	"parent_id"	"abs_parent_id"	"added_at"	"score"	"state_string"	"last_edited_id"	"last_activity_by_id"	"last_activity_at"	"active_revision_id"	"extra"	"extra_ref_id"	"extra_count"	"marked"

# a line from the user data
# "user_ptr_id"	"reputation"	"gold"	"silver"	"bronze"

import sys

forummode = 0
usermode = 0

full_line = ""
for line in sys.stdin:
    # skip the headers of each of the files
    if line.count("node_type", 0, len(line)) == 1:
        forummode = 1
        usermode = 0
        continue

    if line.count("user_ptr_id", 0, len(line)) == 1:
        forummode = 0
        usermode = 1
        continue

    if forummode == 1:
        full_line += line
        data = full_line.strip().split("\t")
        if len(data) == 19:
            # "author_id"   "clasif"    "id"  "title"  "tagnames"    "node_type"  "parent_id"  "abs_parent_id"  "added_at" "score"
            print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}".format(data[3], "B", data[0], data[1], data[2], data[5], data[6], data[7], data[8], data[9])
            full_line = ""

    elif usermode == 1:
        data = line.strip().split("\t")
        # "id"  "clasif"    "reputation"  "gold"  "silver"  "bronze"
        print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(data[0], "A", data[1], data[2], data[3], data[4])

    else:
        print 'buggy'