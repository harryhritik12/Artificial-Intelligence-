import random

def knapsack_local_beam_search(values, weights, weight_limit, k, max_iter):
    n = len(values)
    # generate k random solutions
    solutions = [[random.randint(0, 1) for i in range(n)] for j in range(k)]
    for i in range(max_iter):
        # evaluate the solutions
        scores = [sum([values[j]*solutions[x][j] for j in range(n)]) for x in range(k)]
        # check if any solution exceeds the weight limit
        if any([sum([weights[j]*solutions[x][j] for j in range(n)]) > weight_limit for x in range(k)]):
            # return the best solution
            return solutions[scores.index(max(scores))]
        # select the k best solutions
        best_indices = sorted(range(k), key=lambda x: scores[x], reverse=True)[:k]
        # generate new solutions by flipping a random bit in one of the k best solutions
        new_solutions = []
        for j in range(k):
            x = random.choice(best_indices)
            new_solution = list(solutions[x])
            bit_to_flip = random.randint(0, n-1)
            new_solution[bit_to_flip] = 1 - new_solution[bit_to_flip]
            new_solutions.append(new_solution)
        solutions = new_solutions
    # return the best solution found
    scores = [sum([values[j]*solutions[x][j] for j in range(n)]) for x in range(k)]
    return solutions[scores.index(max(scores))]
# example inputs
values = [10, 20, 30]
weights = [1, 2, 3]
weight_limit = 5
k = 10
max_iter = 100

# run the algorithm
solution = knapsack_local_beam_search(values, weights, weight_limit, k, max_iter)

# print the solution
print(solution)
