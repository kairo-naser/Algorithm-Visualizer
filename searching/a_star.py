# ============================================================
# A* SEARCH ALGORITHM
# ============================================================
# Combines actual cost g(n) + heuristic h(n) = f(n)
# Guarantees shortest path if heuristic is admissible.
# ============================================================
import heapq

def pretty_print_queue(queue):
    """Helper to print the priority queue in readable form."""
    print("Current Queue:")
    for f, g, node, _ in queue:
        print(f"  Node: {node}, f={f}, g={g}")
    print("------------------")

def a_star_search(graph, start, goal, heuristic):
    print("\n==============================")
    print("⭐ A* SEARCH STARTED")
    print(f"Start: {start}, Goal: {goal}")
    print("==============================")

    # Priority Queue stores (f_cost, g_cost, node, path)
    queue = [(heuristic[start], 0, start, [start])]
    visited = set()
    g_costs = {start: 0}

    step = 1

    while queue:
        print(f"\n--- Step {step} ---")
        pretty_print_queue(queue)

        f, g, node, path = heapq.heappop(queue)
        print(f"Visiting node: {node}")
        print(f"  g(n) = {g}, h(n) = {heuristic[node]}, f(n) = {f}")
        print(f"  Path so far: {path}")

        # Goal check
        if node == goal:
            print("\n🎯 Goal Reached!")
            print("✔ Final Path:", path)
            print("✔ Total cost (g):", g)
            return path

        visited.add(node)

        # Expand neighbors
        print(f"Expanding neighbors of {node}...")
        for neighbor, cost in graph[node]:
            tentative_g = g + cost

            better_path = (neighbor not in g_costs) or (tentative_g < g_costs[neighbor])
            if neighbor not in visited and better_path:
                g_costs[neighbor] = tentative_g
                f_cost = tentative_g + heuristic[neighbor]
                new_path = path + [neighbor]

                heapq.heappush(queue, (f_cost, tentative_g, neighbor, new_path))
                print(f"  ➤ Added/Updated {neighbor} in queue with:")
                print(f"      cost so far (g) = {tentative_g}")
                print(f"      heuristic (h) = {heuristic[neighbor]}")
                print(f"      total (f) = {f_cost}")
            else:
                print(f"  ✖ Not adding {neighbor} (visited or not better)")

        step += 1

    print("\n❌ Goal NOT reachable.")
    return None


# Example graph
graph_weighted = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 3)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

heuristic = {'A': 5, 'B': 3, 'C': 2, 'D': 4, 'E': 1, 'F': 0}

# Run A* search
final_path = a_star_search(graph_weighted, 'A', 'F', heuristic)
print("\nResulting Path Returned:", final_path)
