with open('../input/day01_input.txt', 'r') as f:
    previous = f.readline()
    count = 0
    while True:
        current = f.readline()
        if current == '':
            break
        elif int(current) > int(previous):
            count += 1
        previous = current
print(count)
