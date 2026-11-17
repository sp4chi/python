from collections import deque


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]
    ) -> list[bool]:

        # directed ad_list
        ad_list = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            ad_list[u].append(v)

        # generate indegree array
        indegree = [0] * numCourses
        for neighbors in ad_list:
            for neighbor in neighbors:
                indegree[neighbor] += 1

        # maintain a required set array
        required = [set() for _ in range(numCourses)]

        # queue every node with indegree 0
        queue = deque()
        for node in range(len(indegree)):
            if indegree[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()

            for neighbor in ad_list[node]:
                # add node as parent in required set of neighbor
                required[neighbor].add(node)
                # add all the ancestors of node to required set of neighbor
                required[neighbor].update(required[node])

                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        out = [False] * len(queries)

        for i, (u, v) in enumerate(queries):
            if u in required[v]:
                out[i] = True

        return out if len(out) > 0 else [False]
