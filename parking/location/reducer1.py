#!/usr/bin/env python
import sys

current_street = None
current_count = 0
street = None

for line in sys.stdin:

    line = line.strip()

    try:	
    	  street, count = line.split('\t', 1)
    except:
        street, count = "MISSING", 1 

    try:
        count = int(count)
    except ValueError:
        continue

    if current_street == street:
        current_count += count

    else:
        if current_street:
            print("%s\t%s" % (current_street, current_count))
        current_count = count
        current_street = street

if street == current_street:
    print("%s\t%s" % (current_street, current_count))
