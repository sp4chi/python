from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        ad_list = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            ad_list[u].append(v)

        indegrees = [0] * numCourses
        for neighbors in ad_list:
            for neighbor in neighbors:
                indegrees[neighbor] += 1

        queue = deque()
        for node, value in enumerate(indegrees):
            if value == 0:
                queue.append(node)

        order = []
        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in ad_list[node]:
                indegrees[neighbor] -= 1

                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        return True if len(order) == numCourses else False
