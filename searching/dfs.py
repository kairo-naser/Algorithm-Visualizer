# ============================================================
# DEPTH-FIRST SEARCH (DFS) ALGORITHM
# ============================================================
# DFS explores as deep as possible before backtracking.
# Useful for pathfinding in graphs.
# ============================================================

def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    path.append(start)
    visited.add(start)
    print(f"[DFS] Visiting {start}, Path so far: {path}")

    if start == goal:
        print("🎯 Goal Found! Final Path:", path)
        return True

    for neighbor in graph[start]:
        if neighbor not in visited:
            found = dfs(graph, neighbor, goal, visited, path)
            if found:
                return True

    path.pop()
    print(f"[DFS] Backtracking from {start}")
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph, 'A', 'F')
