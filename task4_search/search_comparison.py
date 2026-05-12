from collections import deque

# The Graph (represented as an adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(start_node):
    visited = []
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited

def dfs(start_node, visited=None):
    if visited is None:
        visited = []
    if start_node not in visited:
        visited.append(start_node)
        for neighbor in graph[start_node]:
            dfs(neighbor, visited)
    return visited

print("--- Task 4: BFS vs DFS Comparison ---")
print(f"BFS Traversal (Wide): {bfs('A')}")
print(f"DFS Traversal (Deep): {dfs('A')}")