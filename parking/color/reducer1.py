#!/usr/bin/env python
import sys

current_color = None
current_count = 0
street = None

for line in sys.stdin:

    line = line.strip()

    try:	
    	  color, count = line.split('\t', 1)
    except:
        color, count = "MISSING", 1 

    try:
        count = int(count)
    except ValueError:
        continue

    if current_color == color:
        current_count += count

    else:
        if current_color:
            print("%s\t%s" % (current_color, current_count))
        current_count = count
        current_color = color

if color == current_color:
    print("%s\t%s" % (current_color, current_count))
