#!/usr/bin/python

import sys

previous_forum_id = None
previous_forum_length = 0
total_answers_length = 0    # it will accumulate the full length of all the answers for a parent node
total_answers_count = 0     # it will accumulate the total number of answers for a parent node

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    forum_id, classifier, length = data_mapped

    if previous_forum_id and previous_forum_id != forum_id:
        if total_answers_count > 0:
            print "{0}\t{1}\t{2}".format(previous_forum_id, previous_forum_length, total_answers_length / total_answers_count)
        else:
            print "{0}\t{1}\t{2}".format(previous_forum_id, previous_forum_length, 0)

        # reset
        previous_forum_length = 0
        total_answers_length = 0
        total_answers_count = 0

    if classifier == 'A':
        previous_forum_length = length
    else:
        total_answers_length += float(length)
        total_answers_count += 1

    previous_forum_id = forum_id

if previous_forum_id != None:
    if total_answers_count > 0:
        print "{0}\t{1}\t{2}".format(previous_forum_id, previous_forum_length, total_answers_length / total_answers_count)
    else:
        print "{0}\t{1}\t{2}".format(previous_forum_id, previous_forum_length, 0)