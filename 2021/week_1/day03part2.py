with open('../input/day03_input.txt', 'r') as f:
    measurements = f.read().split("\n")

measurements.pop()

def finder(measurements, most=True, i=0):
    ones = [0] * 12
    zeroes = [0] * 12
    while len(measurements) > 1:
        for measurement in measurements:
            if measurement[i] == '1':
                ones[i] += 1
            else:
                zeroes[i] += 1
        if ones[i] >= zeroes[i]:
            match = '1'
        else:
            match = '0'
        if not most:
            match = str(abs(int(match) - 1))
        measurements = list(filter(lambda measurement: measurement[i] == match, measurements))
        i += 1
    return measurements[0]


o2 = int(finder(measurements, most=True), 2)
co2 = int(finder(measurements, most=False), 2)
print(o2 * co2)
