from itertools import queue
nodes = 5
edges = [[0, 1], [1, 3], [0, 2], [2, 4]]
ad_list = [[] for _ in range(nodes)]
visited = [False] * nodes

for u, v in edges:
    ad_list[u].append(v)
    ad_list[v].append(u)


def bfs(node):
    visited[node] = True
    print(node)
    queue.append(node)

    while queue:
        node = queue[]
