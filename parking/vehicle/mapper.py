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
        issue_date = line[4][-4:]
    except:
        issue_date = "nd"
    
    try:
        vehicle = line[6]
    except:
        vehicle = "nv"

    row = ('%s, %s' % (issue_date, vehicle))
    
    print('%s\t%s' % (row, 1))

