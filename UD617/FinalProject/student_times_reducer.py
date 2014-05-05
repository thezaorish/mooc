#!/usr/bin/python

# Input: student id    time of post
# Output: student id    preferred hour for posting

import sys

previous_user_id = None
hours_with_counts_per_user = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    user_id, hour = data_mapped

    if previous_user_id and previous_user_id != user_id:
        # creating a list of preferred hours for posting, ordered descending by number of posts in that hour
        preferred_hours_desc = sorted(hours_with_counts_per_user, key=lambda t: hours_with_counts_per_user[t], reverse=True)

        max_count = 0
        for key_hour in preferred_hours_desc:
            hour_count = hours_with_counts_per_user[key_hour]

            # identifying the top hours
            if hour_count >= max_count:
                print "{0}\t{1}".format(previous_user_id, key_hour)
                max_count = hour_count
            else:
                break
        hours_with_counts_per_user = {}

    previous_user_id = user_id

    if hour in hours_with_counts_per_user:
        hours_with_counts_per_user[hour] += 1
    else:
        hours_with_counts_per_user[hour] = 1

if previous_user_id != None:
    # creating a list of preferred hours for posting, ordered descending by number of posts in that hour
    preferred_hours_desc = sorted(hours_with_counts_per_user, key=lambda t: hours_with_counts_per_user[t], reverse=True)

    max_count = 0
    for key_hour in preferred_hours_desc:
        hour_count = hours_with_counts_per_user[key_hour]

        # identifying the top hours
        if hour_count >= max_count:
            print "{0}\t{1}".format(previous_user_id, key_hour)
            max_count = hour_count
        else:
            break