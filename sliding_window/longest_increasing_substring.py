class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        ans, left, right = 0, 0, 0
        # increment right on unique characters
        # increment left on duplicate characters
        # window length right - left ( right - left + 1 sometimes but i incremented right before window calculation)
        while right < len(s):
            if s[right] in unique:
                unique.discard(s[left])
                left += 1

            else:
                unique.add(s[right])
                right += 1
                ans = max(ans, right - left)

        return ans
