# edges = [[0, 1], [0, 2], [1, 3], [2, 4]]
edges = [[0, 1], [1, 3], [0, 2], [2, 4], [5, 6], [5, 7], [6, 7]]
nodes = 8
ad_list = [[] for _ in range(nodes)]
components = 0

for u, v in edges:
    ad_list[u].append(v)
    ad_list[v].append(u)


visited = [False] * nodes
print(visited)


def dfs(node):
    visited[node] = True
    print(node)

    neighbours = ad_list[node]
    for neighbour in neighbours:
        if not visited[neighbour]:
            dfs(neighbour)


for node in range(nodes):
    if not visited[node]:
        components += 1
        dfs(node)

print(f"Connected Components {components}")
