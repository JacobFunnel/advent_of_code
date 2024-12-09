from parse import parse_lines

disk_map = [(v, i % 2, i // 2) for i, v in enumerate(parse_lines()[0])]
blocks = []
for v, type_, id_ in disk_map:
    if type_ == 0:
        # id
        blocks.extend([id_] * int(v))
    else:
        # space
        blocks.extend([""] * int(v))

while True:
    block = blocks.pop()
    if block == "":
        continue
    try:
        first_empty_index = blocks.index("")
        blocks[first_empty_index] = block
    except ValueError:
        blocks.append(block)
        break

print(sum(idx * id_ for idx, id_ in enumerate(blocks)))