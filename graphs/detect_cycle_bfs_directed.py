from collections import deque

edge_list = [[0, 1], [0, 2], [1, 3]]  # tree
edge_list_cycle = [[0, 1], [1, 0]]  # cycle


def find_nodes(edges):
    sett = set()
    for edge in edges:
        sett.add(edge[0])
        sett.add(edge[1])
    return sett


def generate_adjacency_list(edges):
    nodes = len(find_nodes(edges))
    ad_list = [[] for _ in range(nodes)]
    for u, v in edges:
        ad_list[u].append(v)
    return ad_list


def bfs(ad_list) -> list[int] | None:
    print(ad_list)
    N = len(ad_list)
    print(N)
    queue = deque()

    # if y is neighbour of x then y has an incoming edge
    indegree = [0] * N
    for node in range(N):
        for nbr in ad_list[node]:
            indegree[nbr] += 1

    # add nodes with in degree 0 to queue
    for node in range(N):
        if indegree[node] == 0:
            queue.append(node)

    order = []
    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbour in ad_list[node]:
            indegree[neighbour] -= 1

            if indegree[neighbour] == 0:
                queue.append(neighbour)

    # only adding nodes to order list whose in degree is 0, hence if nodes participate in a cycle their in degree never decrease to 0, also downstream nodes of a cycle also remain unprocessed, hence length of order list in graphs with cycle have short length
    if len(order) < N:
        return None  # cycle
    return order  # no cycle


result = bfs(generate_adjacency_list(edge_list))
result_1 = bfs(generate_adjacency_list(edge_list_cycle))

print("Cycle detected" if not result else "No Cycle")
print("Cycle detected" if not result_1 else "No Cycle")
