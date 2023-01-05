with open("input/10.txt", "r") as f:
    instructions = [line.split() for line in f.read().splitlines()]


def calc_sig_st(sequence):
    cycle = 1
    x = 1
    signal_strength = 0

    def check_cycle():
        nonlocal signal_strength
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal_strength += cycle * x

    for instruction in sequence:
        if cycle >= 220:
            return signal_strength
        check_cycle()
        if instruction == ["noop"]:
            cycle += 1
        else:
            for _ in range(2):
                if _ == 1:
                    x += int(instruction[1])
                cycle += 1
                check_cycle()


print(calc_sig_st(instructions))
