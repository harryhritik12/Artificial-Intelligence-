import random

def set_covering_local_beam_search(universe, subsets, k, max_iter):
    # initialize k randomly selected states
    current_states = [set(random.sample(range(len(subsets)), len(universe))) for _ in range(k)]
    
    # evaluate the cost of each state
    costs = [len(s) for s in current_states]
    
    # initialize the best state and its cost
    best_state = None
    best_cost = float('inf')
    
    # perform local beam search for max_iter iterations
    for i in range(max_iter):
        # keep the k best current states
        best_indices = sorted(range(len(current_states)), key=lambda i: costs[i])[:k]
        current_states = [current_states[i] for i in best_indices]
        costs = [costs[i] for i in best_indices]
        
        # if all current states have the same cost, return the best state found so far
        if len(set(costs)) == 1:
            return best_state
        
        # generate k new states from the current states
        new_states = []
        for s in current_states:
            for j in range(len(subsets)):
                new_s = s.union([j])
                new_cost = len(new_s)
                new_states.append((new_s, new_cost))
                
        # keep the k best new states
        new_states.sort(key=lambda x: x[1])
        current_states = [s for s, _ in new_states[:k]]
        costs = [c for _, c in new_states[:k]]
        
        # update the best state and its cost
        if costs[0] < best_cost:
            best_state = current_states[0]
            best_cost = costs[0]
            
    return best_state

universe = set(range(1, 11))
subsets = [set([1, 2, 3, 4]), set([3, 4, 5]), set([4, 5, 6, 7]), set([7, 8, 9, 10]), set([6, 7, 8])]
k = 5
max_iter = 100

solution = set_covering_local_beam_search(universe, subsets, k, max_iter)

print(solution)
