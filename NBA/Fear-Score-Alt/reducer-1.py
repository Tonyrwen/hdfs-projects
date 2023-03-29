#!/usr/bin/python3
# Reducer 1
from operator import itemgetter
import sys

players_encounter_result = {}  # it will store the reducer output
reducer_result = ""
for line in sys.stdin:
    try:
        player_set, shot_counter = line.split("\t")
        shot_counter = int(shot_counter)
        if players_encounter_result.get(player_set):
            players_encounter_result[player_set]["total_shots"] += 1
            players_encounter_result[player_set]["shots_made"] += shot_counter
        else:
            players_encounter_result[player_set] = {
                "total_shots": 1,
                "shots_made": shot_counter,
            }
    except ValueError:
        pass

for player_set in players_encounter_result:
    print(
        f"{player_set}\t{players_encounter_result[player_set]['shots_made']}\t{players_encounter_result[player_set]['total_shots']}"
    )
