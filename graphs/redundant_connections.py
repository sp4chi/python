class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:

        n = len(edges)
        parent = [i for i in range(n + 1)]

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(a, b):
            a, b = find(a), find(b)

            if a == b:
                return False
            parent[a] = b
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []
