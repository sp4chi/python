class Solution:
    def maxArea(self, height: list[int]) -> int:
        N = len(height)
        lo, hi = 0, N - 1
        summ = 0
        ht, wh = 0, 0
        while lo < hi:
            ht = min(height[lo], height[hi])
            wh = hi - lo
            area = ht * wh
            summ = max(summ, area)

            if height[lo] <= height[hi]:
                lo += 1
            else:
                hi -= 1
        return summ
