from dataclasses import dataclass

from parse import parse_lines


@dataclass
class Block:
    idx: int
    size: int
    id_: int | None
    type_: str


files, moved_files, empties = [], [], []
absolute_idx = 0
for i, size in enumerate(parse_lines()[0]):
    if i % 2 == 0:
        files.append(Block(absolute_idx, int(size), i // 2, "file"))
    else:
        empties.append(Block(absolute_idx, int(size), None, "empty"))
    absolute_idx += int(size)
#
# disk_map = [[i, int(size), i % 2, i // 2] for i, size in enumerate(parse_lines()[0])]
# absolute_idx = 0
# for entity in disk_map:
#     relative_idx, size, *_ = entity
#     entity[0] = absolute_idx
#     absolute_idx += size
# files  = [[idx, size, id_] for idx, size, type_, id_ in disk_map if type_ == 0]
# empties = [[idx, size, None] for idx, size, type_, id_ in disk_map if type_ == 1]
moved_files = []

while files:
    file = files.pop()
    for empty in empties:
        if empty.size >= file.size and file.idx > empty.idx:
            file.idx = empty.idx
            remaining_empty = empty.size - file.size
            if remaining_empty:
                empty.idx += file.size
                empty.size = remaining_empty
                empties.append(Block(file.idx + file.size, remaining_empty, None, "empty"))
            else:
                empties.remove(empty)
            break
    moved_files.append(file)

print(sorted(moved_files + empties, key=lambda x: x.idx))

check_sum = 0
for file in sorted(moved_files, key=lambda x: x.idx):
        for idx in range(file.idx, file.idx + file.size):
            check_sum += file.idx * file.id_

print(check_sum)
