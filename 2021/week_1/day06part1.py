with open('../input/day06_input.txt', 'r') as f:
    population = [int(x) for x in f.readline().split(',')]

days = 80
new_fish = 0

for day in range(days):
    for i in range(len(population)):
        if population[i] == 0:
            population[i] = 6
            new_fish += 1
        else:
            population[i] -= 1
    for i in range(new_fish):
        population.append(8)
    new_fish = 0

print(len(population))
