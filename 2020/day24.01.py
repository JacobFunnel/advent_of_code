from math import sin, cos, radians

with open("input/24.txt", "r") as f:
    lines = [[char for char in line.strip()] for line in f.readlines()]

angles = {
    "e": (cos(0), sin(0)),
    "ne": (cos(radians(60)), sin(radians(60))),
    "nw": (cos(radians(120)), sin(radians(120))),
    "w": (cos(radians(180)), sin(radians(180))),
    "sw": (cos(radians(240)), sin(radians(240))),
    "se": (cos(radians(300)), sin(radians(300))),
}


def parse(lines):
    global angles
    tile_directions = []
    for line in lines:
        tile_direction = []
        while len(line):
            if len(line) == 1:
                tile_direction.append(line.pop(0))
            elif "".join(line[:2]) in angles:
                tile_direction.append(line.pop(0) + line.pop(0))
            else:
                tile_direction.append(line.pop(0))
        tile_directions.append(tile_direction)
    return tile_directions


lines = parse(lines)
black_tiles = set()
for line in lines:
    pos = [0, 0]
    for direction in line:
        pos = [pos[0] + angles[direction][0], pos[1] + angles[direction][1]]
    tile = (round(pos[0], 2), round(pos[1], 2))
    if tile in black_tiles:
        black_tiles.discard(tile)
    else:
        black_tiles.add(tile)
print(len(black_tiles))
