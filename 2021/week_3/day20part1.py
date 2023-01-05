with open('../input/day20_input.txt', 'r') as f:
    algo = [1 if char == '#' else 0 for char in f.readline().strip()]
    f.readline()
    image = [[1 if char == '#' else 0 for char in line.strip()] for line in f.readlines()]

