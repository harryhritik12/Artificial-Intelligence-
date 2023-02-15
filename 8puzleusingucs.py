from queue import PriorityQueue

def uniform_cost_search(start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in get_neighbors(current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far

def get_neighbors(state):
    zero_index = state.index(0)
    neighbors = []

    if zero_index > 2:
        up = list(state)
        up[zero_index], up[zero_index - 3] = up[zero_index - 3], up[zero_index]
        neighbors.append(tuple(up))

    if zero_index < 6:
        down = list(state)
        down[zero_index], down[zero_index + 3] = down[zero_index + 3], down[zero_index]
        neighbors.append(tuple(down))

    if zero_index not in [0, 3, 6]:
        left = list(state)
        left[zero_index], left[zero_index - 1] = left[zero_index - 1], left[zero_index]
        neighbors.append(tuple(left))

    if zero_index not in [2, 5, 8]:
        right = list(state)
        right[zero_index], right[zero_index + 1] = right[zero_index + 1], right[zero_index]
        neighbors.append(tuple(right))

    return neighbors

def heuristic(goal, next):
    return sum([1 for (g, n) in zip(goal, next) if g != n])

start = (1, 2, 3, 4, 5, 6, 7, 0, 8)
goal = (1, 2, 3, 4, 5, 6, 0, 7, 8)
came_from, cost_so_far = uniform_cost_search(start, goal)
print(came_from)
print('\ns')
print("cost",cost_so_far)
