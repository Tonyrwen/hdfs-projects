#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
from operator import itemgetter

defenders = {}

for line in sys.stdin:
    pair, shooting_data = line.strip().split('\t')
    _, defender = pair.split('-')
    shots, successful = shooting_data.split(',')
    current = defenders.get(defender, [0, 0])
    try:
        current[0] += int(shots) 
        current[1] += int(successful)
        defenders[defender] = current
    except ValueError:
        pass

rates = []
for key, value in defenders.items():
    if value[0] < 10:
        continue
    rates.append([key, float(value[1])/value[0], value[0]])
rates.sort(key=itemgetter(1))

for defender, rate, shots in rates[:5]:
    print('{}\t{:.2%}\t{:,d}'.format(defender, rate, shots))

"""
import sys
from operator import itemgetter


def get_defender_stats(defender_data):
    try:
        shots, successful = defender_data.split(',')
        return int(shots), int(successful)
    except ValueError:
        return 0, 0


def process_input_line(line, defenders):
    pair, shooting_data = line.strip().split('\t')
    _, defender = pair.split('-')
    shots, successful = get_defender_stats(shooting_data)
    current = defenders.get(defender, [0, 0])
    current[0] += shots
    current[1] += successful
    defenders[defender] = current


def calculate_defender_rates(defenders):
    rates = []
    for key, value in defenders.items():
        if value[0] < 10:
            continue
        rate = float(value[1]) / value[0]
        rates.append([key, rate, value[0]])
    return sorted(rates, key=itemgetter(1))


def print_top_defender_rates(rates):
    for defender, rate, shots in rates[:5]:
        print('{}\t{:.2%}\t{:,d}'.format(defender, rate, shots))


def run_map_reduce():
    defenders = {}
    for line in sys.stdin:
        process_input_line(line, defenders)
    defender_rates = calculate_defender_rates(defenders)
    print_top_defender_rates(defender_rates)


if __name__ == '__main__':
    run_map_reduce()
"""