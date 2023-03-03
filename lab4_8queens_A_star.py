import heapq

class QueensNode:
    def __init__(self, state, h=None):
        self.state = state
        self.h = h if h is not None else self.calculate_h()
        self.g = 0
        self.f = self.h
    
    def __eq__(self, other):
        return self.state == other.state
    
    def __hash__(self):
        return hash(str(self.state))
    
    def calculate_h(self):
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
        return self.h == 0
    
    def __lt__(self, other):
        return self.f < other.f
    
class AStar:
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
            explored.add(current_node)
            if current_node.is_goal():
                self.goal_node = current_node
                return self.goal_node
            successors = current_node.get_successors()
            for successor in successors:
                if successor not in explored:
                    successor.g = current_node.g + 1
                    successor.f = successor.g + successor.h
                    heapq.heappush(frontier, successor)
        return None

# Example usage
initial_state = [0, 1, 2, 3, 4, 5, 6, 7]
solver = AStar(initial_state)
solution_node = solver.solve()
if solution_node is None:
    print("Failed to find a solution.")
else:
    print(solution_node.state)
