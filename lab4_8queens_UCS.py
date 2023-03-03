import heapq

class QueensNode:
    def __init__(self, state):
        self.state = state
        self.g = 0
    
    def __eq__(self, other):
        return self.state == other.state
    
    def __hash__(self):
        return hash(str(self.state))
    
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
        conflicts = 0
        for i in range(len(self.state)):
            for j in range(i+1, len(self.state)):
                if self.state[i] == self.state[j] or abs(i-j) == abs(self.state[i]-self.state[j]):
                    conflicts += 1
        return conflicts == 0
    
    def __lt__(self, other):
        return self.g < other.g
    
class UCS:
    def __init__(self, initial_state):
        self.initial_node = QueensNode(initial_state)
        self.goal_node = None
        
    def solve(self):
        """Returns the goal node if a solution is found, None otherwise."""
        frontier = []
        heapq.heappush(frontier, self.initial_node)
        explored = set()
        while frontier:
            current_node = heapq.heappop(frontier)
            if current_node.is_goal():
                self.goal_node = current_node
                return self.goal_node
            explored.add(current_node)
            successors = current_node.get_successors()
            for successor in successors:
                if successor not in explored and successor not in frontier:
                    successor.g = current_node.g + 1
                    heapq.heappush(frontier, successor)
                elif successor in frontier and successor.g > current_node.g + 1:
                    frontier.remove(successor)
                    successor.g = current_node.g + 1
                    heapq.heappush(frontier, successor)
        return None

# Example usage
initial_state = [0, 1, 2, 3, 4, 5, 6, 7]
solver = UCS(initial_state)
solution_node = solver.solve()
if solution_node is None:
    print("Failed to find a solution.")
else:
    print(solution_node.state)
