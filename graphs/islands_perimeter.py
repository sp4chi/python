class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 1
            # visited islands return 0
            if grid[i][j] == -1:
                return 0
            grid[i][j] = -1  # visited
            a = dfs(i - 1, j)  # left
            b = dfs(i, j - 1)  # top
            c = dfs(i + 1, j)  # right
            d = dfs(i, j + 1)  # down

            return a + b + c + d

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    cnt += dfs(row, col)
        return cnt
