class state:
    def __init__(Self, disk, tower, cost=0, heuristic=0):
        Self.disk = disk
        Self.tower = tower
        Self.cost = cost
        Self.heuristic = heuristic

    def __lt__(Self, other):
        return (Self.cost+Self.heuristic) < (other.cost+other.heuristic)

def towerofhanoi(n, start, goal):
    rods = [[], [], []]
    rods[start].extend(range(n, 0, -1))
    initial_state = state(n, rods, 0, (n*(n+1))//2)
    visited = set()
    queue = [initial_state]
    while queue:
        State = queue.pop(0)
        if len(State.tower) > goal and State.tower[goal] == list(range(n, 0, -1)):
            return State.cost

        visited.add(tuple((map(tuple, State.tower))))
        for i, rod_i in enumerate(State.tower):
            if (rod_i):
                for j, rods_j in enumerate(State.tower):
                    if i != j and (not rods_j or rods_j[-1] > rod_i[-1]):
                        new_rods = [rods[:] for rods in State.tower]
                        if len(new_rods[i]) > 0:
                            disk = new_rods[i].pop(0)
                            new_rods[j].append(disk)
                            new_state = state(n, new_rods, State.cost+1, 0)
                            if tuple(map(tuple, new_rods)) not in visited:
                                new_state.heuristic = new_state.cost + \
                                    (n-len(new_rods[goal]))*2
                                queue.append(new_state)

        queue.sort()

    return None


#n = 5
#start = 0
#goal = 2
n = 2  # number of disks
start = 2  # index of starting rod (0, 1, or 2)
goal = 1 

moves = towerofhanoi(n, start, goal)
print(moves)
