with open("input/07.txt", "r") as f:
    t_lines = [line.split(" ") for line in f.read().splitlines()]

current_path = ""
file_system = {}
total_sizes = {}

for line in t_lines:
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "/":
                pass
            elif line[2] == "..":
                current_path = current_path[:current_path.rfind("/")]
            else:
                current_path += "/" + line[2]
        elif line[1] == "ls":
            pass
    elif line[0] == "dir":
        file_system.setdefault(current_path + "/" + line[1], [])
    else:
        file_system.setdefault(current_path, []).append((int(line[0]), line[1]))

for path in file_system.keys():
    total_sizes[path] = sum(
        sum(size for size, name in v)
        for k, v in file_system.items() if path in k
    )

print(sum(size for size in total_sizes.values() if size <= 100000))
