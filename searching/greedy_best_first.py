# ============================================================
# GREEDY BEST-FIRST SEARCH
# ============================================================
# Always chooses the node with smallest heuristic h(n)
# Does NOT guarantee shortest path
# ============================================================

import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    print("\n==============================")
    print("🟩 GREEDY BEST-FIRST SEARCH")
    print(f"Start: {start}, Goal: {goal}")
    print("==============================")

    queue = [(heuristic[start], start, [start])]
    visited = set()
    step = 1

    while queue:
        h, node, path = heapq.heappop(queue)
        print(f"\nStep {step}: Visiting {node}, h={h}, Path={path}")

        if node == goal:
            print("🎯 Goal Found! Final Path:", path)
            return True

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (heuristic[neighbor], neighbor, path + [neighbor]))
                print("Queue updated:", queue)
        step += 1

    print("❌ Goal NOT found")
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

heuristic = {'A': 5, 'B': 3, 'C': 2, 'D': 4, 'E': 1, 'F': 0}
greedy_best_first_search(graph, 'A', 'F', heuristic)
