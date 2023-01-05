with open('../input/day17_input.txt', 'r') as f:
    in_put = f.readline().split()

x_range = [int(x) for x in in_put[2][2:-1].split('..')]
y_range = [int(y) for y in in_put[3][2:].split('..')]


def xshoot(vx):
    if vx < 0:
        direction = -1
    else:
        direction = 1
    x = 0
    t = 0
    in_target = []
    while vx != 0:
        t += 1
        x += vx
        if vx != 0:
            vx -= direction
        if x_range[0] <= x <= x_range[1]:
            in_target.append((True, x, t))
        elif x >= x_range[1]:
            in_target.append((False, None, t))
            return in_target
    return in_target


def yshoot(vy):
    y = 0
    t = 0
    in_target = []
    while True:
        t += 1
        y += vy
        vy -= 1
        if y_range[0] <= y <= y_range[1]:
            in_target.append((True, y, t))
        elif y <= y_range[0]:
            in_target.append((False, None, t))
            return in_target


def shooting_gallery(shoot, low, high):
    valid_shots = []
    terminal_velocities = {}
    for v in range(low, high+1):
        shots = shoot(v)
        tmax = float('inf')
        tmin = float('inf')
        for shot in shots:
            success, distance, time = shot
            tmin = time if time < tmin else tmin
            tmax = time if not distance else tmax
            if success:
                valid_shots.append((v, time))
        if tmax == float('inf') and len(shots):
            terminal_velocities[v] = tmin
    return valid_shots, terminal_velocities


xshots, terminal_vx = shooting_gallery(xshoot, 1, x_range[1])
yshots, terminal_vy = shooting_gallery(yshoot, y_range[0], 150)

ytimes = {t for v, t in yshots}
sucessful_shots = []
for time in ytimes:
    vx_set = {(vx, t) for (vx, t) in xshots if t == time or vx in terminal_vx}
    vy_set = {(vy, t) for (vy, t) in yshots if t == time}
    for vx, tx in vx_set:
        for vy, ty in vy_set:
            if tx == ty:
                sucessful_shots.append((vx, vy))
            elif vx in terminal_vx and terminal_vx[vx] <= ty:
                sucessful_shots.append((vx, vy))


print(len(set(sucessful_shots)))
