class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        m, n = len(image), len(image[0])
        start = image[sr][sc]

        if start == color:
            return image

        # visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or image[i][j] != start:
                return

            # visited[i][j] = True
            image[i][j] = color
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)

        dfs(sr, sc)
        return image
