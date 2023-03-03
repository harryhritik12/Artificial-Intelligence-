import random

class PuzzleNode:
    def __init__(self, state, parent=None, cost=0): 
        self.state = state
        self.parent = parent
        self.cost = cost
    
    def __eq__(self, other):
        return self.state == other.state
    
    def __hash__(self):
        return hash(str(self.state))
    
    def misplaced_tiles(self, goal_state):
        """Heuristic function that returns the number of tiles that are not in their correct position."""
        return sum([1 for i in range(9) if self.state[i] != goal_state[i]])
    
    def get_successors(self):
        """Returns a list of successor nodes."""
        successors = []
        i = self.state.index(0)
        if i not in [0, 1, 2]:  # up
            new_state = list(self.state)
            new_state[i], new_state[i-3] = new_state[i-3], new_state[i]
            successors.append(PuzzleNode(new_state, self, self.cost+1))
        if i not in [0, 3, 6]:  # left
            new_state = list(self.state)
            new_state[i], new_state[i-1] = new_state[i-1], new_state[i]
            successors.append(PuzzleNode(new_state, self, self.cost+1))
        if i not in [2, 5, 8]:  # right
            new_state = list(self.state)
            new_state[i], new_state[i+1] = new_state[i+1], new_state[i]
            successors.append(PuzzleNode(new_state, self, self.cost+1))
        if i not in [6, 7, 8]:  # down
            new_state = list(self.state)
            new_state[i], new_state[i+3] = new_state[i+3], new_state[i]
            successors.append(PuzzleNode(new_state, self, self.cost+1))
        return successors
    
    def is_goal(self, goal_state):
        """Returns True if the node represents the goal state, False otherwise."""
        return self.state == goal_state
    
    def __lt__(self, other):
        return self.misplaced_tiles(goal_state) < other.misplaced_tiles(goal_state)
    
def steepest_ascent_hill_climbing(initial_state, goal_state):
    current_node = PuzzleNode(initial_state)
    best_node = None
    while True:
        if current_node.is_goal(goal_state):
            return current_node
        successors = current_node.get_successors()
        best_successor = min(successors)#, key=lambda node: node.misplaced_tiles(goal_state))
        if best_successor.misplaced_tiles(goal_state) >= current_node.misplaced_tiles(goal_state):
            if best_node is not None:
                return best_node  # return the best node found so far
            else:
                return None  # stuck on a local maximum
        current_node = best_successor
        if best_node is None or best_successor.misplaced_tiles(goal_state) < best_node.misplaced_tiles(goal_state):
            best_node = best_successor
# Example usage
initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal_state = [1, 2, 3, 4, 5, 8, 6, 0, 7]
solution_node = steepest_ascent_hill_climbing(initial_state, goal_state)
if solution_node is None:
    print("No solution found.")
else:
    path = []
    node = solution_node
    while node is not None:
        path.append(node)
        node = node.parent
    path.reverse()
    for node in path:
        print(node.state)
        
