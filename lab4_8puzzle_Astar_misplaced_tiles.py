import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = 0
        self.h = self.heuristic()
        
    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)
        
    def __eq__(self, other):
        return self.state == other.state
        
    def __hash__(self):
        return hash(str(self.state))
        
    def is_goal(self):
        return self.state == (0, 1, 2, 3, 4, 5, 6, 7, 8) 
    
    def heuristic(self):
        # Misplaced tiles heuristic
        h = 0 
        goal=(0,1,2,3,4,5,6,7,8)
        for i in range(9):
            if self.state[i] != 0 and self.state[i] != goal[i]:
                h += 1
        return h
    
    def get_successors(self):
        successors = []
        i = self.state.index(0)
        if i not in [0, 1, 2]:
            new_state = list(self.state)
            new_state[i], new_state[i-3] = new_state[i-3], new_state[i]
            successors.append(PuzzleNode(tuple(new_state), parent=self, action='up'))
        if i not in [6, 7, 8]:
            new_state = list(self.state)
            new_state[i], new_state[i+3] = new_state[i+3], new_state[i]
            successors.append(PuzzleNode(tuple(new_state), parent=self, action='down'))
        if i not in [0, 3, 6]:
            new_state = list(self.state)
            new_state[i], new_state[i-1] = new_state[i-1], new_state[i]
            successors.append(PuzzleNode(tuple(new_state), parent=self, action='left'))
        if i not in [2, 5, 8]:
            new_state = list(self.state)
            new_state[i], new_state[i+1] = new_state[i+1], new_state[i]
            successors.append(PuzzleNode(tuple(new_state), parent=self, action='right'))
        return successors
    
    def get_path(self):
        node = self
        path = []
        while node:
            path.append(node)
            node = node.parent
        return list(reversed(path))

def a_star(start_state):
    start_node = PuzzleNode(start_state)
    frontier = [start_node]
    explored = set()
    while frontier:
        node = heapq.heappop(frontier)
        if node.is_goal():
            return node.get_path()
        explored.add(node)
        for successor in node.get_successors():
            if successor in explored:
                continue
            successor.g = node.g + 1
            heapq.heappush(frontier, successor)
    return None

start_state = (1, 0, 3, 4, 2, 5, 7, 8, 6)
path = a_star(start_state)
if path is None:
    print("No solution found")
for i in [0,len(path)-1]:
    print(path[i].state)
