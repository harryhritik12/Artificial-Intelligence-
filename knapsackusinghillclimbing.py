import random

def knapsack_hill_climbing(values, weights, weight_limit, max_iter):
    # initialize a random solution
    current_solution = [random.randint(0, 1) for _ in range(len(values))]

    for i in range(max_iter):
        # generate all neighbors of the current solution by flipping one bit
        neighbors = [current_solution[:j] + [1 - current_solution[j]] + current_solution[j+1:] for j in range(len(current_solution))]

        # evaluate the value and weight of each neighbor
        neighbor_values = [sum([values[j] for j in range(len(current_solution)) if neighbors[i][j] == 1]) for i in range(len(neighbors))]
        neighbor_weights = [sum([weights[j] for j in range(len(current_solution)) if neighbors[i][j] == 1]) for i in range(len(neighbors))]

        # find the neighbor with the highest value that is within the weight limit
        best_neighbor = None
        best_value = -1
        for i in range(len(neighbors)):
            if neighbor_weights[i] <= weight_limit and neighbor_values[i] > best_value:
                best_neighbor = neighbors[i]
                best_value = neighbor_values[i]

        # if no better neighbor is found, return the current solution
        if best_value <= sum([values[j] for j in range(len(current_solution)) if current_solution[j] == 1]):
            return current_solution

        # otherwise, update the current solution
        current_solution = best_neighbor

    # if the max number of iterations is reached, return the current solution
    return current_solution
values = [10, 20, 30, 40, 50]
weights = [5, 10, 15, 20, 25]
weight_limit = 50
max_iter = 1000

solution = knapsack_hill_climbing(values, weights, weight_limit, max_iter)
print(solution)
