class Solution:
    def trap(self, height: list[int]) -> int:
        N = len(height)
        height_left = [0] * N  # 0 0 1 1 2 2 2 2 3 3 3 3
        height_right = [0] * N  # 3 3 3 3 3 3 3 2 2 2 1 0
        trapped = 0

        height_left[0] = height[0]
        for i in range(1, N):
            height_left[i] = max(height_left[i - 1], height[i])

        height_right[-1] = height[-1]
        for i in range(N - 2, -1, -1):
            height_right[i] = max(height_right[i + 1], height[i])

        for i in range(N):
            pot = min(height_left[i], height_right[i])
            trapped += max(0, pot - height[i])

        return trapped
