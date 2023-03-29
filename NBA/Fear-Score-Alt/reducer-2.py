#!/usr/bin/python3
# Reducer 2
from operator import itemgetter
import sys

fear_score_result = {}  # it will store the reducer output
for line in sys.stdin:
    try:
        player_set, hit_rate = line.split("\t")
        player_A, player_B = player_set.split("->")
        hit_rate = float(hit_rate)

        if fear_score_result.get(player_A):
            if hit_rate < fear_score_result[player_A]["fear_score"]:
                fear_score_result[player_set]["fear_score"] = hit_rate
                fear_score_result[player_set]["defender"] = player_B
        else:
            fear_score_result[player_A] = {"fear_score": hit_rate, "defender": player_B}
    except ValueError:
        pass

# print(fear_score_result)
print("Player\t\t\tMost Unwanted Defender")
print("----------------------------------------------")
for player in fear_score_result:
    print(f"{player}\t\t{fear_score_result[player]['defender']}")
