def bellman_ford_standard(n, edges, src) -> list[int] | None:

    distance = [float("inf")] * n
    distance[src] = 0

    # runs n - 1 times or edges a simple graph with n nodes will have
    for _ in range(n - 1):
        for u, v, w in edges:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # detects cycle and sets all distance of nodes related to -ve weight
    # cycle to -ve infinity
    for _ in range(n - 1):
        for u, v, w in edges:
            if distance[u] + w < distance[v]:
                distance[v] = float("-inf")

    return distance


graph_edges = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3),
]

shortest_distances = bellman_ford_standard(5, graph_edges, src=0)
print(f"Shortest distances from source 0: {shortest_distances}")
# Output: [0, -1, 2, -2, 1]
