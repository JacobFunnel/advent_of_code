from parse import parse_lines


def lavahash(seq):
    value = 0
    for char in seq:
        value = (value + ord(char)) * 17 % 256
    return value


def parse_instruction(seq):
    operation = "-"
    idx = seq.find(operation)
    lens_f = None
    if idx == -1:
        operation = "="
        idx = seq.find(operation)
        lens_f = int(seq[-1])
    label = seq[:idx]
    return operation, label, lens_f


seqs = parse_lines()[0].split(",")
boxes = {}
for seq in seqs:
    operation, label, lens_f = parse_instruction(seq)
    box = lavahash(label)
    if box in boxes and label in (l for l, f in boxes[box]):
        idx = [l for l, f in boxes[box]].index(label)
        if operation == "-":
            boxes[box].pop(idx)
        else:
            boxes[box][idx] = (label, lens_f)
    elif operation == "=":
        boxes.setdefault(box, []).append((label, lens_f))

print(
    sum(
        sum((bi + 1) * (si + 1) * f for si, (l, f) in enumerate(pairs))
        for bi, pairs in boxes.items()
    )
)
