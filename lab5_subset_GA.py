import random

def subset_sum_genetic_algorithm(input_set, target_sum, pop_size=100, max_iterations=1000, mutation_rate=0.01):
    # Define fitness function
    def fitness_function(solution):
        subset_sum = sum(input_set[i] for i in range(len(solution)) if solution[i] == 1)
        fitness = abs(target_sum - subset_sum)
        if subset_sum > target_sum:
            fitness = 0
        return 100 - fitness

    # Generate initial population
    population = []
    for i in range(pop_size):
        solution = [random.randint(0, 1) for _ in range(len(input_set))]
        population.append(solution)

    # Iterate until max_iterations or satisfactory solution found
    for iteration in range(max_iterations):
        # Evaluate fitness of population
        fitness_scores = [fitness_function(solution) for solution in population]

        # Select parents for crossover
        parents = []
        for _ in range(pop_size):
            parent1 = population[random.randint(0, pop_size - 1)]
            parent2 = population[random.randint(0, pop_size - 1)]
            if fitness_function(parent1) > fitness_function(parent2):
                parents.append(parent1)
            else:
                parents.append(parent2)

        # Perform crossover
        new_population = []
        for i in range(pop_size):
            parent1 = parents[random.randint(0, pop_size - 1)]
            parent2 = parents[random.randint(0, pop_size - 1)]
            crossover_point = random.randint(0, len(input_set) - 1)
            child = parent1[:crossover_point] + parent2[crossover_point:]
            new_population.append(child)

        # Perform mutation
        for i in range(pop_size):
            for j in range(len(input_set)):
                if random.random() < mutation_rate:
                    new_population[i][j] = 1 - new_population[i][j]

        # Replace old population with new population
        population = new_population

        # Check for satisfactory solution
        best_solution = max(population, key=fitness_function)
        if fitness_function(best_solution) == 100:
            return [input_set[i] for i in range(len(best_solution)) if best_solution[i] == 1]

    # If no satisfactory solution found, return None
    return None

input_set = [1, 2, 3, 4, 5]
target_sum = 8
subset = subset_sum_genetic_algorithm(input_set, target_sum)
print(subset)