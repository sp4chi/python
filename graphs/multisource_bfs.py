from collections import deque

ad_list = [
    [2, 3],
    [3, 5, 7],
    [0, 4],
    [0, 1, 4],
    [2, 3, 5, 6],
    [1, 4],
    [4],
    [1, 8],
    [7, 9],
    [8],
]
source_nodes = [0, 9]
nodes = 10
distance = [-1 for _ in range(10)]


def bfs(source_nodes):
    queue = deque()

    for node in source_nodes:
        queue.append(node)
        distance[node] = 0

    while queue:
        node = queue.popleft()
        print(node)
        curr_distance = distance[node]

        for neighbour in ad_list[node]:
            if distance[neighbour] == -1:
                distance[neighbour] = curr_distance + 1
                queue.append(neighbour)


bfs(source_nodes)
# for node in range(nodes):
#     if distance[node] == -1:
#         bfs(node)
print(distance)
