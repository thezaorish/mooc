#!/usr/bin/python

import sys

TAGS_TO_DISPLAY = 10

previous_tag = None
occurrences_count = 0   # it will accumulate the number of occurrences for one tag
tag_with_counts = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    tag, count = data_mapped

    if previous_tag and previous_tag != tag:
        tag_with_counts[previous_tag] = occurrences_count   # just storing the tags with counts so far

        # reset
        occurrences_count = 0

    previous_tag = tag
    occurrences_count += int(count)

if previous_tag != None:
    tag_with_counts[previous_tag] = occurrences_count

# sorting the tags descending by counts
tag_with_counts_desc = sorted(tag_with_counts, key=lambda t: tag_with_counts[t], reverse=True)

tags_displayed = 0
for key_tag in tag_with_counts_desc:
    tag_count = tag_with_counts[key_tag]
    if tags_displayed < TAGS_TO_DISPLAY:
        print "{0}\t{1}".format(key_tag, tag_count)
        tags_displayed += 1
    else:
        break