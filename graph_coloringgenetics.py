import random

# Define the graph as an adjacency matrix
graph = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

# Define the number of colors and the population size
num_colors = 4
population_size = 10

# Define the fitness function
def fitness_function(individual):
    # Calculate the number of conflicts (adjacent vertices with the same color)
    conflicts = 0
    for i in range(len(graph)):
        for j in range(i+1, len(graph)):
            if graph[i][j] == 1 and individual[i] == individual[j]:
                conflicts += 1
    return 1.0 / (conflicts + 1.0)

# Define the initialization function
def initialize_population():
    # Generate a random initial population
    population = []
    for _ in range(population_size):
        individual = [random.randint(0, num_colors-1) for _ in range(len(graph))]
        population.append(individual)
    return population

# Define the selection function
def selection(population):
    # Select the top two individuals with the highest fitness
    sorted_population = sorted(population, key=lambda individual: fitness_function(individual), reverse=True)
    return sorted_population[:2]

# Define the crossover function
def crossover(parents):
    # Perform one-point crossover
    crossover_point = random.randint(0, len(graph)-1)
    child1 = parents[0][:crossover_point] + parents[1][crossover_point:]
    child2 = parents[1][:crossover_point] + parents[0][crossover_point:]
    return [child1, child2]

# Define the mutation function
def mutation(individual):
    # Mutate one gene (i.e., vertex color)
    gene = random.randint(0, len(graph)-1)
    individual[gene] = random.randint(0, num_colors-1)
    return individual

# Define the main function
def graph_coloring_ga():
    # Initialize the population
    population = initialize_population()

    # Iterate until a solution is found
    while True:
        # Select the parents
        parents = selection(population)

        # Check if a solution has been found
        if fitness_function(parents[0]) == 1.0:
            return parents[0]

        # Perform crossover and mutation to generate the new population
        new_population = []
        for _ in range(population_size - 2):
            offspring = crossover(parents)
            offspring[0] = mutation(offspring[0])
            offspring[1] = mutation(offspring[1])
            new_population.extend(offspring)
        new_population.extend(parents)

        # Set the new population
        population = new_population

# Example usage
solution = graph_coloring_ga()
print("Solution:", solution)
