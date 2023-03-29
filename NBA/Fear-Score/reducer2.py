#!/usr/bin/env python
import sys

dct = {}

for line in sys.stdin:

    player, hit_rate, attempt_defender = line.strip().split(",")
    attempt, defender = attempt_defender.split("\t")

    current_player = dct.get(player, {0:[0,[]]})
    current_stat = current_player.get(hit_rate, [[],[]])
    try:
        current_stat[0].append(int(attempt))
        current_stat[1].append(defender)
        current_player[hit_rate] = current_stat
        dct[player] = current_player
    except ValueError: pass

for key, value in dct.items():
    worst_stat = list(value.items())[1]
    print("PLAYER: %s, DEFENDERS: %s\nATTEMPTS: %s\tACCURACY: %s\n"%(key, worst_stat[1][1], worst_stat[1][0], worst_stat[0]))
