ad_list = [[1, 2], [0], [0]]  # tree
ad_list_cycle = [[1, 2], [0, 2], [0, 1]]  # cycle

nodes = 3
visited = [False] * nodes
visited_cycle = [False] * nodes


def dfs(node, parent, ad_list, visited) -> bool:
    visited[node] = True

    for neighbour in ad_list[node]:
        if visited[neighbour]:
            if neighbour != parent:
                return True
        else:
            if dfs(neighbour, node, ad_list, visited):
                return True

    return False


print("Cycle detected" if dfs(0, -1, ad_list, visited) else "No Cycle")
print("Cycle detected" if dfs(0, -1, ad_list_cycle, visited_cycle) else "No Cycle")
