#!/usr/bin/python3
# Mapper 1
import sys

# Since the first line is the header, let's skip it!
is_first_line = True

# Read every line
for line in sys.stdin:
    if not is_first_line:
        # Since it's a csv file, split lines by comma
        line = line.split(",")
        # Regular has 23 lines
        if len(line) == 23:
            player_A = line[21]
            player_B = f"{line[16].strip()} {line[15].strip()}"
        # There's an sceneraio that defender's name is just Nene
        else:
            player_A = line[20]
            player_B = f"{line[15].strip()}"

        player_A = player_A.strip()
        player_B = player_B.replace('"', "")

        # Making sure we use this as the count.
        shot_result = 0 if line[14] == "missed" else 1

        # Key will be {player_A}->{player_B}
        # Value : Shot result
        print(f"{player_A}->{player_B}\t{shot_result}")

    else:
        is_first_line = False
