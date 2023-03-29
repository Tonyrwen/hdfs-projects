#!/usr/bin/python3
# Mapper 2
import sys

# Read every line
for line in sys.stdin:
    player_set, shots_made, total_shots = line.split("\t")
    output = f"{player_set}\t {(int(shots_made)/int(total_shots)) * 100}"
    print(output)
