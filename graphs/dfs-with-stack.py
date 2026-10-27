edges = [[0, 1], [1, 3], [0, 2], [2, 4], [5, 6], [5, 7], [6, 7]]
nodes = 8
ad_list = [[] for _ in range(nodes)]
components = 0

for u, v in edges:
    ad_list[u].append(v)
    ad_list[v].append(u)

print(ad_list)

visited = [False] * nodes
print(visited)


def dfs(start):
    stack = [start]

    while stack:
        node = stack.pop()

        visited[node] = True
        print(f"Visited node {node}")

        for neighbour in ad_list[node]:
            if not visited[neighbour]:
                stack.append(neighbour)


for node in range(nodes):
    if not visited[node]:
        components += 1
        dfs(node)

print(f"Connected Components {components}")
