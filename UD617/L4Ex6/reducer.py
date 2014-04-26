#!/usr/bin/python

# from forum data
# "id"  "title"  "tagnames"  "author_id"  "node_type"  "parent_id"  "abs_parent_id"  "added_at" "score"

# from user data
# "reputation"  "gold"  "silver"  "bronze"

import sys

userinfo = None
currentuserid = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if data_mapped[1] == "A":
        # "id"  "clasif"    "reputation"  "gold"  "silver"  "bronze"
        userid, clasif, reputation, gold, silver, bronze = data_mapped
        currentuserid = userid
        userinfo = data_mapped

    elif data_mapped[1] == "B":
        # "author_id"   "clasif"    "id"  "title"  "tagnames"    "node_type"  "parent_id"  "abs_parent_id"  "added_at" "score"
        author_id, clasif, id, title, tagnames, node_type, parent_id, abs_parent_id, added_at, score = data_mapped

        # "id"  "title"  "tagnames"  "author_id"  "node_type"  "parent_id"  "abs_parent_id"  "added_at" "score"  "reputation"  "gold"  "silver"  "bronze"
        print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(id, title, tagnames, author_id, node_type, parent_id, abs_parent_id, added_at, score, userinfo[2], userinfo[3], userinfo[4], userinfo[5])

    else:
        print "buggy"