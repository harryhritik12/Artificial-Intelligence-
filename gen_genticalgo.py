import random
from typing import List, Set

def fitness_function(chromosome: List[int], subsets: List[Set[int]], universe: Set[int]) -> float:
    """Calculates the fitness of a chromosome by computing the number of sets needed to cover the universe."""
    selected_subsets = [subsets[i] for i in range(len(chromosome)) if chromosome[i]]
    covered = set().union(*selected_subsets)
    return len(selected_subsets) + len(universe - covered)

def crossover(parent1: List[int], parent2: List[int]) -> List[int]:
    """Performs a two-point crossover between two parents to create a new child."""
    length = len(parent1)
    crossover_points = sorted(random.sample(range(1, length), 2))
    child = parent1[:crossover_points[0]] + parent2[crossover_points[0]:crossover_points[1]] + parent1[crossover_points[1]:]
    return child

def mutate(chromosome: List[int], mutation_rate: float) -> List[int]:
    """Mutates a chromosome by randomly flipping bits based on the mutation rate."""
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = int(not chromosome[i])
    return chromosome

def set_cover_ga(subsets: List[Set[int]], universe: Set[int], population_size: int, num_generations: int, crossover_rate: float, mutation_rate: float) -> List[int]:
   
    # Create initial population
    population = []
    for i in range(population_size):
        chromosome = [random.randint(0, 1) for _ in range(len(subsets))]
        population.append(chromosome)
    
    # Iterate over generations
    for gen in range(num_generations):
        # Evaluate fitness of each chromosome
        fitness_scores = [fitness_function(chromosome, subsets, universe) for chromosome in population]
        
        # Select parents for reproduction
        parent1, parent2 = random.choices(population, weights=fitness_scores, k=2)
        
        # Perform crossover and mutation to create new children
        child1 = crossover(parent1, parent2)
        child1 = mutate(child1, mutation_rate)
        child2 = crossover(parent2, parent1)
        child2 = mutate(child2, mutation_rate)
        
        # Replace least fit chromosomes with new children
        population[fitness_scores.index(min(fitness_scores))] = child1
        population[fitness_scores.index(min(fitness_scores))] = child2
    
    # Select the best chromosome from the final population as the solution
    fitness_scores = [fitness_function(chromosome, subsets, universe) for chromosome in population]
    best_chromosome = population[fitness_scores.index(min(fitness_scores))]
    
    return best_chromosome
subsets = [{1, 2, 3}, {2, 4}, {3, 4, 5}, {4, 5}, {5, 6}]
universe = {1, 2, 3, 4, 5, 6}
population_size = 100
num_generations = 100
crossover_rate = 0.8
mutation_rate = 0.1

solution = set_cover_ga(subsets, universe, population_size, num_generations, crossover_rate, mutation_rate)

print(solution)
