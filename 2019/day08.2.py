with open("input/08.txt", "r") as f:
    numbers = [int(n) for n in f.read().strip()]

width, height = 25, 6
layers = int(len(numbers) / (width * height))


def reduce_layer(layer):
    for i, pixel in enumerate(layer):
        if pixel != 2:
            return pixel


pixels = [reduce_layer(numbers[i::layers]) for i in range(width * height)]
pp = {0: " ", 1: "#"}
for i, pixel in enumerate(pixels):
    if i % width == width - 1:
        end = "\n"
    else:
        end = ""
    print(pp[pixel], end=end)
