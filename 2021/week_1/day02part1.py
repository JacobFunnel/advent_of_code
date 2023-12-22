horizontal = 0
depth = 0
with open("../input/day02_input.txt", "r") as f:
    while True:
        try:
            direction, value = f.readline().split(" ")
            if direction == "forward":
                horizontal += int(value)
            elif direction == "up":
                depth -= int(value)
            elif direction == "down":
                depth += int(value)
        except:
            break

print(horizontal * depth)
