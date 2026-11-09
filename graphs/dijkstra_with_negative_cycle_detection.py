import heapq


def SSSP(graph, source) -> tuple:
    n = len(graph)
    parent = [-1] * n
    distance = [float("inf")] * n
    distance[source] = 0

    # Track how many times each node's distance is successfully updated
    update_count = [0] * n
    update_count[source] = 1

    min_heap = []
    heapq.heappush(min_heap, (0, source))

    while min_heap:
        dist, node = heapq.heappop(min_heap)

        if dist > distance[node]:
            continue

        for neighbor, weight in graph[node]:
            new_distance = dist + weight

            if new_distance < distance[neighbor]:
                # If a node gets updated V or more times, a negative cycle exists
                if update_count[neighbor] >= n:
                    raise ValueError(
                        "Negative weight cycle detected! Shortest paths are undefined."
                    )

                parent[neighbor] = node
                distance[neighbor] = new_distance
                update_count[neighbor] += 1  # Increment the update counter

                heapq.heappush(min_heap, (new_distance, neighbor))

    return (distance, parent)


def find_shortest_path(graph, source, target) -> list:
    try:
        distance, parent = SSSP(graph, source)
    except ValueError as e:
        print(e)
        return []

    path = []
    if distance[target] == float("inf"):
        return path

    current_node = target
    while current_node != -1:
        path.append(current_node)
        current_node = parent[current_node]

    return path[::-1]


# Test Graph with a Negative Cycle:
# Node 0 -> Node 1 (weight 3)
# Node 1 -> Node 2 (weight 2)
# Node 2 -> Node 1 (weight -4) <-- Forms a negative loop with Node 1
graph_with_cycle = [
    [(1, 3)],  # Node 0 connects to 1
    [(2, 2)],  # Node 1 connects to 2
    [(1, -4)],  # Node 2 connects back to 1 (Cycle cost = -2)
]

print(find_shortest_path(graph_with_cycle, 0, 2))
