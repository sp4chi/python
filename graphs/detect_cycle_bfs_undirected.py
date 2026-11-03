from collections import deque

ad_list = [[1, 2], [0], [0]]  # tree
ad_list_cycle = [[1, 2], [0, 2], [0, 1]]  # cycle

nodes = 3
visited = [False] * nodes
visited_cycle = [False] * nodes


def bfs(
    node,
    ad_list,
    visited,
) -> bool:
    queue = deque()
    visited[node] = True
    queue.append((node, -1))

    while queue:
        node, parent = queue.popleft()

        for neighbour in ad_list[node]:
            print(
                f"Node {node} Parent {parent} Neighbour {neighbour} Visited {visited[neighbour]}"
            )
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append((neighbour, node))

            else:
                if parent != neighbour:
                    return True
    return False


for node in range(nodes):
    if not visited[node]:
        print("Cycle detected" if bfs(node, ad_list, visited) else "No Cycle")
        print(
            "Cycle detected" if bfs(node, ad_list_cycle, visited_cycle) else "No Cycle"
        )
