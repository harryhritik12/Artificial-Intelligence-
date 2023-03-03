import random

def subset_sum_hill_climbing(numbers, target_sum, max_iterations):
    best_subset = set(random.sample(numbers, random.randint(1, len(numbers))))
    best_diff = abs(sum(best_subset) - target_sum)
    
    for i in range(max_iterations):
        next_subset = best_subset.copy()
        if random.random() < 0.5:
            # add or remove a number from the subset
            if len(next_subset) == 1:
                next_subset.add(random.choice(numbers))
            else:
                next_subset.remove(random.choice(list(next_subset)))
        else:
            # swap a number in the subset with one not in the subset
            swap = False
            while not swap:
                num1 = random.choice(list(next_subset))
                num2 = random.choice([n for n in numbers if n not in next_subset])
                if num1 != num2:
                    next_subset.remove(num1)
                    next_subset.add(num2)
                    swap = True
        
        next_diff = abs(sum(next_subset) - target_sum)
        if next_diff < best_diff:
            best_subset = next_subset
            best_diff = next_diff
            
            if best_diff == 0:
                return best_subset
    
    return None
numbers = [1, 2, 3, 4, 5]
target_sum = 9
ans=subset_sum_hill_climbing(numbers, target_sum, 10000)
print(ans)