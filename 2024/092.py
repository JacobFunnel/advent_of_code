from parse import parse_lines

disk_map = [[i, int(size), ['file', 'empty'][i % 2], i // 2] for i, size in enumerate(parse_lines()[0])]
absolute_idx = 0
for entity in disk_map:
    relative_idx, size, *_ = entity
    entity[0] = absolute_idx
    absolute_idx += size

class Block:
    def __init__(self, idx, size, id_, type_):
        self.idx = idx
        self.size = size
        self.id_ = id_
        self.type_ = type_

    def get_properties(self):
        return self.idx, self.size, self.id_, self.type_

files  = [Block(idx, size, id_, type_) for idx, size, type_, id_ in disk_map if type_ == 'file']
empties = [Block(idx, size, None, type_) for idx, size, type_, id_ in disk_map if type_ == 'empty']
moved_files = []



while files:
    file = files.pop()
    file_idx, file_size, file_id, _ = file.get_properties()
    for empty in empties:
        empty_idx, empty_size, empty_id, __ = empty.get_properties()
        if empty_size >= file_size and file_idx > empty_idx:
            file.idx = empty_idx
            remaining_empty = empty_size - file_size
            if remaining_empty:
                empty.idx = empty_idx + file_size
                empty.size = remaining_empty
            else:
                empties.remove(empty)
            break
    moved_files.append(file)

blocks = sorted(moved_files + empties, key=lambda x: x.idx)
check_sum = 0
for block in blocks:
    absolute_idx, size, id_, type_ = block.get_properties()
    if type_ == 'file':
        for idx in range(absolute_idx, absolute_idx + size):
            check_sum += idx * id_

print(check_sum)
