from collections import deque

edge_list = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 4], [3, 5], [4, 5], [5, 6]]

nodes = 7

# 0 -> [1,2]
# 1 -> [3]
# 2 -> [3, 4]
# 3 -> [5]
# 4 -> [5]
# 5 -> [6]
# 6 -> []


def generate_adjacency_list(nodes, edges) -> list[list[int]]:
    ad_list = [[] for _ in range(nodes)]
    for u, v in edges:
        ad_list[u].append(v)
    return ad_list


def top_sort(ad_list) -> list[int] | None:
    N = len(ad_list)

    indegrees = [0] * N

    # if y is neighbour of x, y has an in degree of 1
    for neighbours in ad_list:
        for neighbour in neighbours:
            indegrees[neighbour] += 1
    print(f"Indegrees {indegrees}")

    # add nodes with indegree 0 to the queue
    queue = deque()
    for node, indegree in enumerate(indegrees):
        if indegree == 0:
            queue.append(node)

    order = []
    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbour in ad_list[node]:
            indegrees[neighbour] -= 1

            if indegrees[neighbour] == 0:
                queue.append(neighbour)

    return order if len(order) == N else None


print(f"Order {top_sort(generate_adjacency_list(nodes, edge_list))}")
