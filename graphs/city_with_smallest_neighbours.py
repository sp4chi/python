class Solution:
    def findTheCity(
        self, n: int, edges: list[list[int]], distanceThreshold: int
    ) -> int:
        # using floyd warshall (Tc - O(v^3))

        # 1. converting ad-list to adjacency matrix
        distance = [[float("inf")] * n for _ in range(n)]
        # a. setting distance of node to itself 0
        for i in range(n):
            distance[i][i] = 0

        # b. copy edges from input graph to distance
        for u, v, w in edges:
            distance[u][v] = w
            distance[v][u] = w
        # c. run the algo
        row, col = len(distance), len(distance[0])  # optional
        for k in range(n):
            for i in range(row):
                for j in range(col):
                    # if distance of i-k and k-j is less than i-j, new smaller path from
                    # i-j found through k, relax that edge
                    if distance[i][k] + distance[k][j] < distance[i][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]

        # 2. find latest city with the smallest number of neighbours at a distance given
        city = 0
        neighbours = float("inf")
        for u in range(n):
            cnt = 0
            for v in range(n):
                if 0 < distance[u][v] <= distanceThreshold:
                    cnt += 1
            if cnt <= neighbours:
                neighbours = cnt
                city = u
        return city
