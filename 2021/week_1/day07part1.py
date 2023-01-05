with open('../input/day07_input.txt', 'r') as f:
    positions = [int(x) for x in f.readline().split(',')]

efforts = []

for target_pos in range(min(positions), max(positions)+1):
    fuel = 0
    for position in positions:
        fuel += abs(target_pos - position)
    efforts.append(fuel)

print(min(efforts))
