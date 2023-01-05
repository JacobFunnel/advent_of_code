with open('../input/day08_input.txt', 'r') as f:
    codes = [[b.split() for b in a.split('|')] for a in f.readlines()]

total = 0

for in_put, out_put in codes:
    in_chars = [{char for char in digit} for digit in in_put]
    out_chars = [{char for char in digit} for digit in out_put]
    digits = {str(i): None for i in range(10)}
    digits['1'] = list(filter(lambda x: len(x) == 2, in_chars))[0]
    digits['7'] = list(filter(lambda x: len(x) == 3, in_chars))[0]
    digits['4'] = list(filter(lambda x: len(x) == 4, in_chars))[0]
    digits['8'] = list(filter(lambda x: len(x) == 7, in_chars))[0]
    len5 = list(filter(lambda x: len(x) == 5, in_chars))
    len6 = list(filter(lambda x: len(x) == 6, in_chars))
    len5diff = (len5[0] | len5[1] | len5[2]) - (len5[0] & len5[1] & len5[2])
    len6diff = (len6[0] | len6[1] | len6[2]) - (len6[0] & len6[1] & len6[2])
    d = len6diff - len5diff

    for i in range(len(len6)):
        if not d.issubset(len6[i]):
            digits['0'] = len6[i]
            len6.pop(i)
            break

    for i in range(len(len6)):
        if digits['7'].issubset(len6[i]):
            digits['9'] = len6[i]
            len6.pop(i)
            digits['6'] = len6[0]
            break
    while len(len5) > 0:
        for i in range(len(len5)):
            if len(digits['6'] & len5[i]) == 5:
                digits['5'] = len5[i]
                len5.pop(i)
                break
            elif len(digits['1'] & len5[i]) == 2:
                digits['3'] = len5[i]
                len5.pop(i)
                break
            else:
                digits['2'] = len5[i]
                len5.pop(i)
                break
    out_number = ''
    for entry in out_chars:
        out_number += list(digits.keys())[list(digits.values()).index(entry)]
    total += int(out_number)

print(total)


"""
segments = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
length_5 = {2, 3, 5}
length_5_differences = {'b', 'c', 'e', 'f'}
length_6 = {0, 6, 9}
length_6_differences = {'c', 'd', 'e'}
"""

