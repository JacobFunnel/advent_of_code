with open("input/10.txt", "r") as f:
    instructions = [line.split() for line in f.read().splitlines()]


def get_pixels(sequence):
    cycle = 1
    pixels = "⬛"
    x = 1

    def next_cycle():
        nonlocal cycle, pixels
        pixels += "⬛" if cycle % 40 in [x - 1, x, x + 1] else "⬜"
        cycle += 1

    for instruction in sequence:
        if instruction == ["noop"]:
            next_cycle()
        else:
            for _ in range(2):
                if _ == 1:
                    x += int(instruction[1])
                next_cycle()

    return pixels


image = get_pixels(instructions)
for i, pixel in enumerate(image[:-1]):
    if i % 40 == 0:
        print("")
    print(pixel, end="")

