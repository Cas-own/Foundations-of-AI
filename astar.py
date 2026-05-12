import heapq

def a_star_search(graph, heuristics, start, goal):
    # priority_queue = [(f_score, current_node, path, g_score)]
    # f(n) = g(n) + h(n)
    priority_queue = [(heuristics[start], start, [start], 0)]
    visited = set()

    while priority_queue:
        (f_score, current, path, g_score) = heapq.heappop(priority_queue)

        if current in visited:
            continue
        
        if current == goal:
            return path, g_score

        visited.add(current)

        for neighbor, weight in graph.get(current, {}).items():
            new_g = g_score + weight
            new_f = new_g + heuristics.get(neighbor, 0)
            heapq.heappush(priority_queue, (new_f, neighbor, path + [neighbor], new_g))

    return None, float('inf')

# --- TEST DATA ---
# Adjacency list: { Node: {Neighbor: Cost} }
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'D': 8, 'E': 4},
    'C': {'G': 10},
    'D': {'G': 1},
    'E': {'G': 5},
    'G': {}
}
# Heuristic values (estimated distance to goal G)
heuristics = {'A': 10, 'B': 8, 'C': 5, 'D': 1, 'E': 3, 'G': 0}

path, cost = a_star_search(graph, heuristics, 'A', 'G')
print(f"Optimal Path: {path}")
print(f"Total Cost: {cost}")