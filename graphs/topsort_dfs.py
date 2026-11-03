ad_list = [[1, 2], [2, 3], [4], [], []]  # output - [0,1,2,4,3]


def dfs(node, ad_list, visited_nodes, visited) -> void:
    visited[node] = True

    for neighbour in ad_list[node]:
        if not visited[neighbour]:
            dfs(neighbour, ad_list, visited_nodes, visited)
    visited_nodes.append(node)


def top_sort(ad_list) -> list[int]:
    nodes = len(ad_list)
    visited = [False] * nodes
    ordering = [0] * nodes
    i = nodes - 1

    for at in range(nodes):
        if not visited[at]:
            visited_nodes = []
            dfs(at, ad_list, visited_nodes, visited)
            for node in visited_nodes:
                ordering[i] = node
                i -= 1
    return ordering


print(top_sort(ad_list))
