class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0

        # 4 - 0 1 2 3 -> [0,1,2], [1,2,3] -> 4-3 = 1
        cnt = 0

        for i in range(len(s) - 3 + 1):
            if len(set(s[i : i + 3])) == 3:
                cnt += 1

        return cnt
