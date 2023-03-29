#!/usr/bin/env python
import sys

pair_dct = {}

for line in sys.stdin:
    pair, shot = line.strip().split("\t")
    made, attempt = shot.split(",")

    current = pair_dct.get(pair, [0,0])
    try:
        current[0] += int(made)
        current[1] += int(attempt)
        pair_dct[pair] = current
    except ValueError: pass

for key, value in pair_dct.items():
    if value[1] < 10: continue
    player, defender = key.split(",")
    hit_rate = float(value[0])/value[1]

    print("%s,%s,%s,%s"%(player, hit_rate, value[1], defender))
