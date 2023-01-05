with open('../input/day06_input.txt', 'r') as f:
    population = [int(x) for x in f.readline().split(',')]

population = {i: population.count(i) for i in range(9)}
days = 256

for day in range(days):
    new_fish = population[0]
    population = {i: population[(i+1)%9] for i in range(9)}
    population[6] += new_fish

print(sum(population.values()))
