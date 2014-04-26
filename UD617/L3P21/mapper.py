#!/usr/bin/python

__author__ = 'training'

# 127.0.0.1 user-identifier frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326
# 10.223.157.186 - - [15/Jul/2009:20:50:29 -0700] "GET / HTTP/1.1" 200 9157

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        host, rfcId, userId, dateTime, timezone, method, resource, protocol, statusCode, size = data
        print "{0}\t{1}".format(resource, 1)