import numpy as np
import time

start_time = time.time()

with open("../input/day25_input.txt", "r") as f:
    grid = np.mat([[c for c in line.strip()] for line in f.readlines()])

rows, columns = np.shape(grid)
east_cumbers = np.argwhere(grid == ">")
east_cumbers = {(pair[0], pair[1]) for pair in np.split(east_cumbers, 1)[0]}
prev_east = east_cumbers.copy()
south_cumbers = np.argwhere(grid == "v")
south_cumbers = {(pair[0], pair[1]) for pair in np.split(south_cumbers, 1)[0]}
prev_south = south_cumbers.copy()
step = 0


def east_step(position):
    r, c = position
    destination = (r, (c + 1) % columns)
    if destination in east_cumbers | south_cumbers:
        destination = position
    return destination


def south_step(position):
    r, c = position
    destination = ((r + 1) % rows, c)
    if destination in east_cumbers | south_cumbers:
        destination = position
    return destination


while True:
    east_destinations = set()
    for east_cumber in east_cumbers:
        east_destinations.add(east_step(east_cumber))
    east_cumbers = east_destinations.copy()

    south_destinations = set()
    for south_cumber in south_cumbers:
        south_destinations.add(south_step(south_cumber))
    south_cumbers = south_destinations.copy()

    step += 1
    if east_cumbers == prev_east and south_cumbers == prev_south:
        print(step)
        print(time.time() - start_time)
        break

    prev_east = east_cumbers.copy()
    prev_south = south_cumbers.copy()
