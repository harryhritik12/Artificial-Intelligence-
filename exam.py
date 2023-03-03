from queue import PriorityQueue

def n_puzzle_ucs(start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = dict()
    cost_so_far = dict()
    came_from[tuple(start)] = None
    cost_so_far[tuple(start)] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == tuple(goal):
            break

        for next in get_neighbors(current):
            new_cost = cost_so_far[tuple(current)] + 1
            if tuple(next) not in cost_so_far or new_cost < cost_so_far[tuple(next)]:
                cost_so_far[tuple(next)] = new_cost
                priority = new_cost
                #frontier.put(tupple(next), priority)
                frontier.put(tuple(next), priority)
                came_from[tuple(next)] = tuple(current)

    return came_from, cost_so_far

def get_neighbors(state):
    n = int(len(state) ** 0.5)
    zero_index = state.index(0)
    neighbors = []

    if zero_index >= n:
        up = list(state)
        up[zero_index], up[zero_index - n] = up[zero_index - n], up[zero_index]
        neighbors.append(tuple(up))

    if zero_index < n * (n - 1):
        down = list(state)
        down[zero_index], down[zero_index + n] = down[zero_index + n], down[zero_index]
        neighbors.append(tuple(down))

    if zero_index % n != 0:
        left = list(state)
        left[zero_index], left[zero_index - 1] = left[zero_index - 1], left[zero_index]
        neighbors.append(tuple(left))

    if zero_index % n != n - 1:
        right = list(state)
        right[zero_index], right[zero_index + 1] = right[zero_index + 1], right[zero_index]
        neighbors.append(tuple(right))

    return neighbors

start = tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])
goal = tuple([12, 1, 2, 15, 11, 6, 5, 8, 7, 10, 9, 4, 0, 13, 14, 3])
solution = n_puzzle_ucs(start, goal)
print(solution)
