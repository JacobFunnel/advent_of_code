with open('../input/day22_input.txt', 'r') as f:
    filelines = [line.split() for line in f.readlines()]

instructions = []

for line in filelines:
    switch, rest = line
    rest = rest.split(',')
    rest = [[xyz[0], *xyz[2:].split('..')] for xyz in rest]
    d = {}
    for xyz in rest:
        d.update({xyz[0]: (int(xyz[1]), int(xyz[2]))})
    instructions.append((switch, d))

instructions = instructions[:20]
on = set()

for switch, reach in instructions:
    to_switch = set()
    for x in range(reach['x'][0], reach['x'][1] + 1):
        for y in range(reach['y'][0], reach['y'][1] + 1):
            for z in range(reach['z'][0], reach['z'][1] + 1):
                to_switch.add((x, y, z))
    if switch == 'on':
        on = on | to_switch
    elif switch == 'off':
        on -= to_switch

print(len(on))
