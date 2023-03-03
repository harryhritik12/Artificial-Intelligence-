import random
import math

# The 8-Queens problem is to place 8 queens on an 8x8 chessboard so that no two queens can attack each other.
# The state is represented as a list of integers, where each integer represents the row position of a queen in the corresponding column.


def random_state():
    # Generate a random initial state
    return [random.randint(0, 7) for _ in range(8)]


def attack_pairs(state):
    # Calculate the number of attacking queen pairs in the state
    count = 0
    for i in range(8):
        for j in range(i+1, 8):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                count += 1
    return count


def simulated_annealing(state, temperature=1.0, cooling_rate=0.99):
    # Simulated Annealing algorithm
    while temperature > 0.1:
        current_score = attack_pairs(state)
        if current_score == 0:
            return state  # Found a solution
        next_state = list(state)
        col = random.randint(0, 7)
        row = random.randint(0, 7)
        next_state[col] = row
        next_score = attack_pairs(next_state)
        delta_e = next_score - current_score
        if delta_e < 0 or math.exp(-delta_e/temperature) > random.random():
            state = next_state
        temperature *= cooling_rate
    return state  # Best state found


# Example usage
initial_state = random_state()
print("Initial state:", initial_state)
solution_state = simulated_annealing(initial_state)
print("Solution state:", solution_state)
print("Attacking pairs:", attack_pairs(solution_state))
