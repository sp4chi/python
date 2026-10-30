class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxx = 0

        def dfs(i, j):
            stack = [(i, j)]
            grid[i][j] = 0
            ans = 0

            while stack:
                i, j = stack.pop()

                if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                    continue

                grid[i][j] = 0
                ans += 1

                stack.append((i, j + 1))
                stack.append((i + 1, j))
                stack.append((i, j - 1))
                stack.append((i - 1, j))

            return ans

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    area = dfs(i, j)
                    maxx = max(maxx, area)
        return maxx
