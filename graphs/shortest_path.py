from collections import deque


def shortest_path(graph, source, destination):
    n = len(graph)
    distance = [-1] * n
    parent = [-1] * n

    queue = deque()
    distance[source] = 0
    queue.append(source)
    parent[source] = -1

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if distance[neighbor] == -1:
                # Assign distance
                distance[neighbor] = distance[node] + 1
                # Add neighbor to queue
                queue.append(neighbor)
                # Assign parent
                parent[neighbor] = node

    if distance[destination] == -1:
        return []

    path = []
    curr = destination
    while curr != -1:
        path.append(curr)
        curr = parent[curr]

    return path[::-1]


ad_list = [[1, 2, 3], [0, 3], [0, 3], [0, 1, 2]]
print(shortest_path(ad_list, 0, 4))
