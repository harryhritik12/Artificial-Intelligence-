import random

W = 50  # Maximum weight that the knapsack can hold
n = 10  # Number of items available
values = [random.randint(1, 10) for _ in range(n)]  # Random values for the items
weights = [random.randint(1, 10) for _ in range(n)]  # Random weights for the items

POPULATION_SIZE = 100  # Number of individuals in the population
NUM_GENERATIONS = 100  # Number of generations to run the genetic algorithm
CROSSOVER_RATE = 0.8  # Probability of performing crossover between two parents
MUTATION_RATE = 0.2  # Probability of mutating an individual in the population


class Chromosome:
    def __init__(self, genes):
        self.genes = genes

    def calculate_fitness(self):
        total_weight = 0
        total_value = 0
        for i in range(n):
            if self.genes[i] == 1:
                total_weight += weights[i]
                total_value += values[i]
        if total_weight > W:
            return 0  # Penalize solutions that exceed the maximum weight
        else:
            return total_value

    def __repr__(self):
        return f"Chromosome({self.genes})"


def initialize_population():
    population = []
    for _ in range(POPULATION_SIZE):
        genes = [random.randint(0, 1) for _ in range(n)]
        chromosome = Chromosome(genes)
        population.append(chromosome)
    return population


def select_parents(population):
    fitnesses = [chromosome.calculate_fitness() for chromosome in population]
    total_fitness = sum(fitnesses)
    probabilities = [fitness / total_fitness for fitness in fitnesses]
    parent1, parent2 = random.choices(population, weights=probabilities, k=2)
    return parent1, parent2


def perform_crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        crossover_point = random.randint(1, n - 1)
        child_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
        child = Chromosome(child_genes)
    else:
        child = Chromosome(parent1.genes)
    return child



def perform_mutation(child):
    if random.random() < MUTATION_RATE:
        mutated_genes = list(child.genes)
        mutation_point = random.randint(0, n - 1)
        mutated_genes[mutation_point] = 1 - mutated_genes[mutation_point]  # Flip the bit at the mutation point
        child = Chromosome(mutated_genes)
    return child


def evolve_population(population):
    new_population = []
    for _ in range(POPULATION_SIZE):
        parent1, parent2 = select_parents(population)
        child = perform_crossover(parent1, parent2)
        if child is not None:
            child = perform_mutation(child)
        new_population.append(child)
    return new_population


def get_best_solution(population):
    best_fitness = 0
    best_chromosome = None
    for chromosome in population:
        fitness = chromosome.calculate_fitness()
        if fitness > best_fitness:
            best_fitness = fitness
            best_chromosome = chromosome
    return best_chromosome, best_fitness


population = initialize_population()
for generation in range(NUM_GENERATIONS):
    population = evolve_population(population)
    best_chromosome, best_fitness = get_best_solution(population)
    print(f"Generation {generation + 1}: Best solution = {best_chromosome}, Fitness = {best_fitness}")

