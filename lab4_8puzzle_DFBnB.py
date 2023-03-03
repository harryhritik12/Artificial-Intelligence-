class PuzzleNode:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = 0
        
    def __eq__(self, other):
        return self.state == other.state
        
    def __hash__(self):
        return hash(str(self.state))
        
    def is_goal(self):
        return self.state == (0, 1, 2, 3, 4, 5, 6, 7, 8)
    
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
    
    def get_f(self, h):
        return self.g + h(self.state)

def misplaced_tiles(state):
    goal=(0,1,2,3,4,5,6,7,8)
    return sum([state[i] != goal[i] for i in range(9)])
# def misplaced_tiles(state):
#     return sum([state[i] != i for i in range(9)])

def depth_first_branch_and_bound(start_state, heuristic):
    start_node = PuzzleNode(start_state)
    path = [start_node]
    min_f = float('inf')
    while path:
        node = path[-1]
        if node.is_goal():
            return node.get_path()
        if node.g + heuristic(node.state) >= min_f:
            path.pop()
            continue
        for successor in node.get_successors():
            if successor in path:
                continue
            successor.g = node.g + 1
            path.append(successor)
        min_f = min([node.get_f(heuristic) for node in path])
    return None

start_state = (1, 0, 2,3,4,5,6,7,8)
path = depth_first_branch_and_bound(start_state,misplaced_tiles)
if path is None:
    print("No solution found")
else:
  for i in [0,len(path)-1]:
      print(path[i].state)
