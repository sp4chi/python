from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        n, m = len(mat), len(mat[0])

        distance = [[-1] * m for _ in range(n)]
        queue = deque()
        for row in range(n):
            for col in range(m):
                if mat[row][col] == 0:
                    distance[row][col] = 0
                    queue.append((row, col))

        while queue:
            r, c = queue.popleft()

            for i, j in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                if 0 <= i < n and 0 <= j < m and distance[i][j] == -1:
                    distance[i][j] = distance[r][c] + 1
                    queue.append((i, j))

        return distance
