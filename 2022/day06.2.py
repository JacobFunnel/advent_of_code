with open("input/06.txt", "r") as f:
    signal = (char for char in f.read())

buffer = ""
for idx, char in enumerate(signal):
    buffer += char
    if idx >= 13 and len(set(buffer[-14:])) == 14:
        print(idx + 1)
        break
