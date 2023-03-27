#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    frequency, street = line.split('\t', 1)
    print("%s\t%s" % (street, frequency))
