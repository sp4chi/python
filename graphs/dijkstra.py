import heapq


# def dijkstra(graph, source):
#     n = len(graph)
#     distance = [float("inf")] * n

#     min_heap = []

#     distance[source] = 0
#     heapq.heappush(min_heap, (0, source))

#     while min_heap:
#         dist, node = heapq.heappop(min_heap)

#         # Skip stale entries
#         if dist > distance[node]:
#             continue

#         for neighbor, weight in graph[node]:
#             # Calculate candidate distance
#             new_distance = distance[node] + weight

#             # Relaxation
#             if new_distance < distance[neighbor]:
#                 distance[neighbor] = new_distance
#                 heapq.heappush(min_heap, (new_distance, neighbor))

#     return distance


def SSSP(graph, source) -> list:
    n = len(graph)
    # init parent list
    parent = [-1] * n

    # init distance list
    distance = [float("inf")] * n
    distance[source] = 0

    # init min_heap
    min_heap = []
    heapq.heappush(min_heap, (0, source))  # O(logn)

    while min_heap:
        dist, node = heapq.heappop(min_heap)  # O(logn)

        # distance[node] : best distance of node so far
        if dist > distance[node]:
            continue

        for neighbor, weight in graph[node]:
            # calculate distance
            new_distance = dist + weight

            # update distance of neighbour and push to min_heap
            if new_distance < distance[neighbor]:
                parent[neighbor] = node
                distance[neighbor] = new_distance
                heapq.heappush(min_heap, (new_distance, neighbor))

    return (distance, parent)


def find_shortest_path(graph, source, target) -> list:
    distance, parent = SSSP(graph, source)
    path = []
    if distance[target] == float("inf"):
        return path

    current_node = target
    while current_node != -1:
        path.append(current_node)
        current_node = parent[current_node]

    return path[::-1]


graph = [[(1, 10), (2, 1)], [], [(1, 1)]]


print(find_shortest_path(graph, 0, 1))
