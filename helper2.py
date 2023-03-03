
	#1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,0, 14, 15
	#12,1,2,15,11,9,10,8,7,6,5,4,0,13,14,3
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
        return self.state == (12,1,2,15,11,9,10,8,7,6,5,4,0,13,14,3) 
    
    def heuristic(self):
        # Misplaced tiles heuristic
        h = 0 
        goal=(12,1,2,15,11,9,10,8,7,6,5,4,0,13,14,3)
        for i in range(16):
            if self.state[i] != 0 and self.state[i] != goal[i]:
                h += 1
        return h
    
    def get_successors(self):
        successors = []
        i = self.state.index(0)
        if i not in [0, 1, 2, 3]:
            new_state = list(self.state)
            new_state[i], new_state[i-4] = new_state[i-4], new_state[i]
            successors.append(PuzzleNode(tuple(new_state), parent=self, action='up'))
        if i not in [12, 13, 14, 15]:
            new_state = list(self.state)
            new_state[i], new_state[i+4] = new_state[i+4], new_state[i]
            successors.append(PuzzleNode(tuple(new_state), parent=self, action='down'))
        if i not in [0, 4, 8, 12]:
            new_state = list(self.state)
            new_state[i], new_state[i-1] = new_state[i-1], new_state[i]
            successors.append(PuzzleNode(tuple(new_state), parent=self, action='left'))
        if i not in [3, 7, 11, 15]:
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
                #successor.g=min(successor.g,node.g+1)
            
                continue
            successor.g = node.g + 1
            heapq.heappush(frontier, successor)
    return None

start_state = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,0)
path = a_star(start_state)
if path is None:
    print("No solution found")
for i in [0,len(path)-1]:
    print(path[i].state)