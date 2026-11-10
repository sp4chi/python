from collections import deque

nodes = 5
edges = [[0, 1], [1, 3], [0, 2], [2, 4]]
ad_list = [[] for _ in range(nodes)]
visited = [False] * nodes


for u, v in edges:
    ad_list[u].append(v)
    ad_list[v].append(u)


def bfs(node):
    queue = deque()
    queue.append(node)

    while queue:
        node = queue.popleft()
        print(node)

        for neighbour in ad_list[node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)


for node in range(nodes):
    if not visited[node]:
        bfs(node)
# expected output - 0 1 2 3 4
