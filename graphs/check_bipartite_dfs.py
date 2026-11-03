def is_bipartite(graph) -> bool:
    N = len(graph)
    color = [-1] * N

    def dfs(node, graph, color) -> bool:
        for neighbor in graph[node]:
            if color[neighbor] == -1:
                color[neighbor] = 1 - color[node]
                if not dfs(neighbor, graph, color):
                    return False
            elif color[neighbor] == color[node]:
                return False
        return True

    for node in range(N):
        if color[node] == -1:
            color[node] = 0
            if not dfs(node, graph, color):
                return False

    return True


graph = [[1, 3], [0, 2], [1, 3], [0, 2]]

print(is_bipartite(graph))

graph = [[1, 2], [0, 2], [0, 1]]

print(is_bipartite(graph))

graph = [[1], [0], [3], [2]]

print(is_bipartite(graph))
