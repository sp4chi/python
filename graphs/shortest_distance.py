from collections import deque

nodes = 5
edges = [[0, 1], [1, 3], [0, 2], [2, 4]]
ad_list = [[] for _ in range(nodes)]


for u, v in edges:
    ad_list[u].append(v)
    ad_list[v].append(u)


def bfs(node, target):
    visited = [False] * nodes
    queue = deque([(node, 0)])
    visited[node] = True

    while queue:
        node, distance = queue.popleft()

        if node == target:
            return distance

        for next in ad_list[node]:
            if not visited[next]:
                visited[next] = True
                queue.append((next, distance + 1))


print(bfs(0, 3))
