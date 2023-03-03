import random

class QueensNode:
    def __init__(self, state, conflicts=None):
        self.state = state
        self.conflicts = conflicts if conflicts is not None else self.calculate_conflicts()
    
    def __eq__(self, other):
        return self.state == other.state
    
    def __hash__(self):
        return hash(str(self.state))
    
    def calculate_conflicts(self):
        """Calculates the number of conflicting queens."""
        conflicts = 0
        for i in range(len(self.state)):
            for j in range(i+1, len(self.state)):
                if self.state[i] == self.state[j] or abs(i-j) == abs(self.state[i]-self.state[j]):
                    conflicts += 1
        return conflicts
    
    def get_successors(self):
        """Returns a list of successor nodes."""
        successors = []
        for i in range(len(self.state)):
            for j in range(len(self.state)):
                if j != self.state[i]:
                    new_state = list(self.state)
                    new_state[i] = j
                    successors.append(QueensNode(new_state))
        return successors
    
    def is_goal(self):
        """Returns True if the node represents a goal state, False otherwise."""
        return self.conflicts == 0
    
    def __lt__(self, other):
        return self.conflicts < other.conflicts
    
def hill_climbing_with_min_conflicts(initial_state, max_steps=1000):
    current_node = QueensNode(initial_state)
    for i in range(max_steps):
        if current_node.is_goal():
            return current_node
        successors = current_node.get_successors()
        best_successor = min(successors)
        if best_successor.conflicts >= current_node.conflicts:
            # Select a random state with minimal conflicts to escape local maxima
            min_conflict_states = [successor for successor in successors if successor.conflicts == current_node.conflicts]
            current_node = random.choice(min_conflict_states)
        else:
            current_node = best_successor
    return None

# Example usage
initial_state = [0, 1, 2, 3, 4, 5, 6, 7]
solution_node = hill_climbing_with_min_conflicts(initial_state)
if solution_node is None:
    print("Failed to find a solution.")
else:
    print(solution_node.state)
