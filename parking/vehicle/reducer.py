#!/usr/bin/python

from operator import itemgetter
import re
import sys

######### reducer #########

dict_date_count = {}

for line in sys.stdin:
    line = line.strip()
    date, num = line.split('\t')
    try:
        num = int(num)
        dict_date_count[date] = dict_date_count.get(date, 0) + num
    except ValueError:
        pass

sorted_dict_date_count = sorted(dict_date_count.items(), key=itemgetter(1))

print(sorted_dict_date_count[-1])
