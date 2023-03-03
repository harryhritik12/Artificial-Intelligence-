import random

def subset_sum_beam_search(numbers, target_sum, k=10, max_iterations=1000):
    # Initialize k random subsets of the input numbers
    subsets = [set(random.sample(numbers, random.randint(1, len(numbers)))) for i in range(k)]
    
    for i in range(max_iterations):
        # Sort the current subsets by how close they are to the target sum
        best_subsets = sorted(subsets, key=lambda s: abs(sum(s) - target_sum))[:k]
        # If one of the best subsets has the target sum, return it
        if any(sum(s) == target_sum for s in best_subsets):
            return next(s for s in best_subsets if sum(s) == target_sum)
        
        # Generate new subsets by adding or removing one number from each of the best subsets
        new_subsets = []
        for subset in best_subsets:
            for number in numbers:
                if number not in subset:
                    new_subsets.append(subset.union({number}))
                if len(subset) > 1:
                    new_subsets.append(subset - {random.choice(tuple(subset))} | {number})
                if number in subset:
                    not_in_subset = list(set(numbers) - subset)
                    if not_in_subset:
                        new_subsets.append((subset - {number}) | {random.choice(not_in_subset)})
        
        # Sort the new subsets by how close they are to the target sum
        subsets = sorted(new_subsets, key=lambda s: abs(sum(s) - target_sum))[:k]
    
    # If no subset is found within the maximum number of iterations, return None
    return None
numbers = [1, 2, 3, 4, 5]
target_sum = 9

result = subset_sum_beam_search(numbers, target_sum)
print(result)
