from collections import deque


def is_bipartite(graph):
    n = len(graph)
    color = [-1] * n

    queue = deque()
    for node in range(n):
        if color[node] == -1:
            color[node] = 0
            queue.append(node)

            while queue:
                node = queue.popleft()

                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)

                    if color[neighbor] == color[node]:
                        return False

    return True


graph = [[1, 3], [0, 2], [1, 3], [0, 2]]

print(is_bipartite(graph))

graph = [[1, 2], [0, 2], [0, 1]]

print(is_bipartite(graph))

graph = [[1], [0], [3], [2]]

print(is_bipartite(graph))
