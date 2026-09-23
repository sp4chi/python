class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        out = []
        nums.sort()
        N = len(nums)
        for i in range(N):
            # if first number is +ve, we can stop the search because 3 +ve numbers do not add upto to zero
            if nums[i] > 0:
                break
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            lo, hi = i + 1, N - 1

            while lo < hi:
                summ = nums[lo] + nums[hi] + nums[i]
                if summ == 0:
                    out.append([nums[i], nums[lo], nums[hi]])

                    lo, hi = lo + 1, hi - 1

                    # skip duplicates
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1

                elif summ < 0:
                    lo += 1
                else:
                    hi -= 1

        return out
