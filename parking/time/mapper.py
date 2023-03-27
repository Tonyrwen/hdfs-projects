#!/usr/bin/python
# --*-- coding:utf-8 --*--

import sys
import csv

header = sys.stdin.readline()

for line in csv.reader(sys.stdin):
    # Remove any leading/trailing whitespaces
    #line = line.strip()

    # Split the line into fields (assuming it's a CSV with comma-separated values)
    #fields = line.split(',')
    try:
        time = line[19][:2]
	apm = line[19][-1]
    except:
	time = "99"
	apm = "9"

    print('%s\t%s' % (time+apm, 1))

