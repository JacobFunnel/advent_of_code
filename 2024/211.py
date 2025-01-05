"""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+

    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""

from parse import parse_lines

codes = parse_lines()[:-1]
keypad = {
    "0": 0,
    "1": -1 + 1j,
    "2": 1j,
    "3": 1 + 1j,
    "4": -1 + 2j,
    "5": 2j,
    "6": 1 + 2j,
    "7": -1 + 3j,
    "8": 3j,
    "9": 1 + 3j,
    "A": 1,
}
dpad = {
    "v": 0,
    "<": -1,
    ">": 1,
    "^": -1j,
    "A": 1 + 1j,
}


def steps_between(a, b):
    a, b = keypad[a], keypad[b]
    return abs(a.real - b.real) + abs(a.imag - b.imag)


print(steps_between("0", "9"))
