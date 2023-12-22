from parse import parse_lines
from itertools import pairwise

value_readings = [[int(n) for n in line.split()] for line in parse_lines()]
prev_values = []
for values in value_readings:
    series = [values]
    while True:
        series.append([b - a for a, b in pairwise(series[-1])])
        if all(n == 0 for n in series[-1]):
            break
    for under, over in pairwise(range(len(series) - 1, -1, -1)):
        series[over].insert(0, series[over][0] - series[under][0])
    prev_values.append(series[0][0])

print(sum(prev_values))
