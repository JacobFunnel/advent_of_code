with open("../input/day17_input.txt", "r") as f:
    in_put = f.readline().split()

y_range = [int(y) for y in in_put[3][2:].split("..")]
valid_vy = []


def yshoot(vy):
    ymax = 0
    y = 0
    t = 0
    while True:
        t += 1
        y += vy
        if y > ymax:
            ymax = y
        vy -= 1
        if y_range[0] <= y <= y_range[1]:
            return True, ymax, t
        elif y <= y_range[0]:
            return False, None, t


for vy in range(y_range[0], 150):
    shot = yshoot(vy)
    if shot[0]:
        valid_vy.append((vy, *shot[1:]))

print(valid_vy[-1][1])
