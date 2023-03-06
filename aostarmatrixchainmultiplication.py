import heapq


class node:
    def __init__(self, start, end, cost, heuristic):
        self.start = start
        self.end = end
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(Self, other):
        return (Self.cost+Self.heuristic) <(other.cost+other.heuristic)


def ao_star_optimal(chain):

    start_node = node(1, len(chain), 0, heuristic(chain))

    frontier = []
    heapq.heappush(frontier, start_node)
    visited = set()
    while frontier:
        current_node = heapq.heappop(frontier)
        if (current_node.start == current_node.end):
            return current_node.cost

        visited.add((current_node.start, current_node.end))
        for i in range(current_node.start, current_node.end):
            for j in range(i, current_node.end):
                if (i, j) in visited:
                    continue
                successor_cost = current_node.cost + \
                    chain[current_node.start-1]*chain[j]*chain[i-1]
                successor_heuristic = heuristic(chain[i:j+1])

                successor_node = node(
                    i+1, j+1, successor_cost, successor_heuristic)
                heapq.heappush(frontier, successor_node)
    return None


def heuristic(chain):

    return 0


chain = [3, 3, 1, 5, 1, 2, 2,9]
min_cost = ao_star_optimal(chain)
print(f"Minimum cost to multiply matrices {chain}: {min_cost}")
