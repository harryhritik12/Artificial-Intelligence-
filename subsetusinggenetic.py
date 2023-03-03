import random

# Define the size of the population and the number of generations
POPULATION_SIZE = 100
NUM_GENERATIONS = 1000

def subset_sum_genetic_algorithm(numbers, target_sum):
    # Initialize the population with random subsets of the numbers
    population = [set(random.sample(numbers, random.randint(1, len(numbers)))) for i in range(POPULATION_SIZE)]
    
    # Iterate over the specified number of generations
    for generation in range(NUM_GENERATIONS):
        # Evaluate the fitness of each individual in the population
        fitness_scores = [abs(target_sum - sum(individual)) for individual in population]
        
        # Select the fittest individuals to serve as parents
        parent_indices = sorted(range(len(fitness_scores)), key=lambda k: fitness_scores[k])[:2]
        parents = [population[i] for i in parent_indices]
        
        # Crossover the parents to generate a new child
        child = parents[0].union(parents[1])
        
        # Mutate the child by adding or removing a random number
        if random.random() < 0.5:
            child.add(random.choice(numbers))
        else:
            child.discard(random.choice(list(child)))
        
        # Replace the least fit individual in the population with the new child
        least_fit_index = max(range(len(fitness_scores)), key=lambda k: fitness_scores[k])
        population[least_fit_index] = child
    
    # Evaluate the fitness of the final population
    fitness_scores = [abs(target_sum - sum(individual)) for individual in population]
    
    # Return the fittest individual, if it has the target sum
    if min(fitness_scores) == 0:
        return population[fitness_scores.index(0)]
    else:
        return None
numbers = [2, 4, 6, 8, 10]
target_sum = 14
ans= subset_sum_genetic_algorithm(numbers, target_sum)
print(ans)