#!/usr/bin/python

import sys

previous_forum_id = None
users_for_post = []     # it will accumulate all the users contributing to the post

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    forum_id, author_id = data_mapped

    if previous_forum_id and previous_forum_id != forum_id:
        print "{0}\t{1}".format(previous_forum_id, users_for_post)
        users_for_post = []

    previous_forum_id = forum_id
    users_for_post.append(int(author_id))

if previous_forum_id != None:
    print "{0}\t{1}".format(previous_forum_id, users_for_post)
