import random

# define the problem parameters
W = 50
n = 10
values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
weights = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# define the genetic algorithm parameters
population_size = 100
mutation_rate = 0.1
generations = 50

# define the fitness function
def fitness(chromosome):
    total_weight = 0
    total_value = 0
    for i in range(n):
        if chromosome[i] == 1:
            total_weight += weights[i]
            total_value += values[i]
    if total_weight > W:
        return 0
    else:
        return total_value

# define the initial population
population = []
for i in range(population_size):
    chromosome = [random.randint(0, 1) for j in range(n)]
    population.append(chromosome)

# run the genetic algorithm
for g in range(generations):
    # evaluate the fitness of each chromosome
    fitness_scores = [fitness(chromosome) for chromosome in population]

    # select the parents
    parents = []
    for i in range(population_size // 2):
        parent1 = random.choices(population, weights=fitness_scores)[0]
        parent2 = random.choices(population, weights=fitness_scores)[0]
        parents.append((parent1, parent2))

    # create the offspring
    offspring = []
    for parent1, parent2 in parents:
        crossover_point = random.randint(1, n-1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        offspring.append(child1)
        offspring.append(child2)

    # mutate the offspring
    for i in range(len(offspring)):
        for j in range(n):
            if random.random() < mutation_rate:
                offspring[i][j] = 1 - offspring[i][j]

    # combine the parent and offspring populations
    combined_population = population + offspring

    # select the new population
    fitness_scores = [fitness(chromosome) for chromosome in combined_population]
    sorted_population = [chromosome for _, chromosome in sorted(zip(fitness_scores, combined_population), reverse=True)]
    population = sorted_population[:population_size]

# print the best solution found
best_fitness = max([fitness(chromosome) for chromosome in population])
best_chromosome = [chromosome for chromosome in population if fitness(chromosome) == best_fitness][0]
print("Best solution found: ", best_chromosome)
print("Total value: ", best_fitness)
