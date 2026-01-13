# ============================================================
# A* SEARCH ALGORITHM
# ============================================================
# Combines actual cost g(n) + heuristic h(n) = f(n)
# Guarantees shortest path if heuristic is admissible.
# ============================================================

import heapq

def a_star_search(graph, start, goal, heuristic):
    print("\n==============================")
    print("⭐ A* SEARCH")
    print(f"Start: {start}, Goal: {goal}")
    print("==============================")

    # Priority Queue stores (f_cost, g_cost, node, path)
    queue = [(heuristic[start], 0, start, [start])]
    visited = set()
    g_costs = {start: 0}
    step = 1

    while queue:
        f, g, node, path = heapq.heappop(queue)
        print(f"\nStep {step}: Visiting {node}, g={g}, h={heuristic[node]}, f={f}, Path={path}")

        if node == goal:
            print("🎯 Goal Found! Final Path:", path)
            return True

        visited.add(node)

        for neighbor, cost in graph[node]:
            tentative_g = g + cost
            if neighbor not in visited or tentative_g < g_costs.get(neighbor, float('inf')):
                g_costs[neighbor] = tentative_g
                f_cost = tentative_g + heuristic[neighbor]
                heapq.heappush(queue, (f_cost, tentative_g, neighbor, path + [neighbor]))
                print("Queue updated:", queue)

        step += 1

    print("❌ Goal NOT found")
    return False

graph_weighted = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 3)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

heuristic = {'A': 5, 'B': 3, 'C': 2, 'D': 4, 'E': 1, 'F': 0}
a_star_search(graph_weighted, 'A', 'F', heuristic)
