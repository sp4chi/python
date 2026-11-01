from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        FRESH, ROTTEN, EMPTY = 1, 2, 0
        m, n = len(grid), len(grid[0])
        fresh = 0
        queue = deque()

        for row in range(m):
            for col in range(n):
                if grid[row][col] == ROTTEN:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        if fresh == 0:
            return 0

        min_time = -1
        while queue:
            min_time += 1
            for rot in range(len(queue)):
                r, c = queue.popleft()

                for r, c in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        fresh -= 1
                        grid[r][c] = ROTTEN
                        queue.append((r, c))

        return min_time if fresh == 0 else -1
