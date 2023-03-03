from queue import PriorityQueue

def is_valid(state):
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                return False
    return True

def ucs_search():
    start_state = ()
    frontier = PriorityQueue()
    frontier.put((0, start_state))
    explored = set()

    while not frontier.empty():
        cost, state = frontier.get()

        if state in explored:
            continue

        if len(state) == 8:
            return state

        explored.add(state)

        for i in range(8):
            if i not in state:
                child = state + (i,)
                if is_valid(child):
                    frontier.put((cost+1, child))

    return None

solution = ucs_search()
if solution:
    print("Found solution: ", solution)
else:
    print("No solution found.")
