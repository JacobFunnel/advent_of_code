from parse import parse_lines

OPERANDS = {"AND": lambda x, y: x & y, "OR": lambda x, y: x | y, "XOR": lambda x, y: x ^ y}
raw_wires, raw_gates = parse_lines(2)
wires = {pair[:3]: int(pair[-1]) for pair in raw_wires.splitlines()}
gates = [triplet.split(" ") for triplet in raw_gates.splitlines() if triplet]
gates = {gate: (OPERANDS[op], g1, g2) for g1, op, g2, _, gate in gates}


def evaluate(gate):
    try:
        op, g1, g2 = gates[gate]
    except KeyError:
        return wires[gate]
    if isinstance(g1, str):
        g1 = evaluate(g1)
    if isinstance(g2, str):
        g2 = evaluate(g2)
    return op(g1, g2)


s = ""
for gate in sorted((k for k in gates.keys() if k.startswith("z")), reverse=True):
    s += str(evaluate(gate))

print(int(s, 2))
