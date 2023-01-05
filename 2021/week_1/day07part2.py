with open('../input/day07_input.txt', 'r') as f:
    positions = [int(x) for x in f.readline().split(',')]

efforts = []

for target_pos in range(min(positions), max(positions)+1):
    fuel = 0
    for position in positions:
        fuel += (abs(target_pos - position)*(abs(target_pos - position)+1))/2
    efforts.append(fuel)

print(int(min(efforts)))

"""
Formula for summing consecutive natural numbers:
sum = n(A1+An)/2
if A1 = n and An = 0 then:
sum = n(n+1)/2
"""