from parse import parse_lines

disk_map = [[i, int(size), i % 2, i // 2] for i, size in enumerate(parse_lines()[0])]
absolute_idx = 0
for entity in disk_map:
    relative_idx, size, *_ = entity
    entity[0] = absolute_idx
    absolute_idx += size
files  = [[idx, size, id_] for idx, size, type_, id_ in disk_map if type_ == 0]
empties = [[idx, size, None] for idx, size, type_, id_ in disk_map if type_ == 1]
moved_files = []

while files:
    file = files.pop()
    file_idx, file_size, file_id = file
    for empty in empties:
        empty_idx, empty_size, empty_id = empty
        if empty_size >= file_size and file_idx > empty_idx:
            file_idx = empty_idx
            remaining_empty = empty_size - file_size
            if remaining_empty:
                empty[0] = empty_idx + file_size
                empty[1] = remaining_empty
            else:
                empties.remove(empty)
            break
    moved_files.append([file_idx, file_size, file_id])

blocks = sorted(moved_files + empties, key=lambda x: x[0])
check_sum = 0
for absolute_idx, size, id_ in blocks:
    if id_:
        for idx in range(absolute_idx, absolute_idx + size):
            check_sum += idx * id_

print(check_sum)
