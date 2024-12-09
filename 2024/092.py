from dataclasses import dataclass

from parse import parse_lines

@dataclass
class Block:
    idx: int
    size: int
    id_: int
    type_: str

disk_map = [Block(i, int(size), i // 2, ['file', 'empty'][i % 2]) for i, size in enumerate(parse_lines()[0])]
absolute_idx = 0
for block in disk_map:
    block.idx = absolute_idx
    absolute_idx += block.size
files  = [block for block in disk_map if block.type_ == 'file']
empties = [block for block in disk_map if block.type_ == 'empty']
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
            else:
                empties.remove(empty)
            break
    moved_files.append(file)

blocks = sorted(moved_files + empties, key=lambda x: x.idx)
check_sum = 0
for block in blocks:
    if block.type_ == 'file':
        for idx in range(block.idx, block.idx + block.size):
            check_sum += block.idx * block.id_

print(check_sum)
