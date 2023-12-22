horizontal = 0
depth = 0
aim = 0
with open("../input/day02_input.txt", "r") as f:
    while True:
        try:
            direction, value = f.readline().split(" ")
            value = int(value)
            if direction == "forward":
                horizontal += value
                depth += aim * value
            elif direction == "up":
                aim -= value
            elif direction == "down":
                aim += value
        except:
            break

print(horizontal * depth)
