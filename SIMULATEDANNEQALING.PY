import random
import math

# Evaluate the quality of a given state
def evaluate_state(state):
    # Count the number of tiles out of place
    count = 0
    for i in range(9):
        if state[i] != i:
            count += 1
    return count

# Generate all possible successor states
def generate_successors(state):
    successors = []
    i = state.index(0)
    if i % 3 > 0:
        # Move the tile to the left
        new_state = state[:]
        new_state[i], new_state[i-1] = new_state[i-1], new_state[i]
        successors.append(new_state)
    if i % 3 < 2:
        # Move the tile to the right
        new_state = state[:]
        new_state[i], new_state[i+1] = new_state[i+1], new_state[i]
        successors.append(new_state)
    if i // 3 > 0:
        # Move the tile up
        new_state = state[:]
        new_state[i], new_state[i-3] = new_state[i-3], new_state[i]
        successors.append(new_state)
    if i // 3 < 2:
        # Move the tile down
        new_state = state[:]
        new_state[i], new_state[i+3] = new_state[i+3], new_state[i]
        successors.append(new_state)
    return successors

# Generate a random initial state
def generate_initial_state():
    state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    random.shuffle(state)
    return state

# Perform Simulated Annealing to solve the puzzle
def simulated_annealing():
    # Generate a random initial state
    current_state = generate_initial_state()
    
    # Set the initial temperature and cooling rate
    temperature = 1.0
    cooling_rate = 0.0005
    
    # Loop until we reach the goal state
    while evaluate_state(current_state) > 0 and temperature > 1e-9:
        # Generate a random successor state
        next_state = random.choice(generate_successors(current_state))
        
        # Calculate the energy difference between the current and successor states
        delta_energy = evaluate_state(next_state) - evaluate_state(current_state)
        
        # If the successor is better, move to it
        if delta_energy < 0:
            current_state = next_state
        # If the successor is worse, move to it with a certain probability
        else:
            probability = math.exp(-delta_energy / temperature)
            if random.random() < probability:
                current_state = next_state
        
        # Decrease the temperature
        temperature *= 1 - cooling_rate
        
    return current_state

# Run the solver and print the results
solution = simulated_annealing()
print("Solution:", solution)
