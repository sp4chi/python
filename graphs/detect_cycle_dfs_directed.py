from collections import deque

ad_list = [[1, 2], [3], [], []]
ad_list_cycle = [[1, 2], [3], [3], [2]]
nodes = 4
state = [0] * nodes
state_cycle = [0] * nodes

# 0 - unvisited
# 1 - in stack
# 2 - dfs finished


def dfs(node, ad_list, state) -> bool:
    state[node] = 1

    for neighbour in ad_list[node]:
        if state[neighbour] == 1:
            return True

        if not state[neighbour]:
            if dfs(neighbour, ad_list, state):
                return True

    state[node] = 2
    return False


print("Cycle detected" if dfs(0, ad_list, state) else "No Cycle")
print("Cycle detected" if dfs(0, ad_list_cycle, state_cycle) else "No Cycle")
