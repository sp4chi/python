from typing import List


def removeElement(nums: List[int], val: int) -> int:
    n = len(nums)
    k = 0
    left = 0
    for right in range(0, n):
        if nums[right] != val:
            nums[left] = nums[right]
            left += 1
    return left


l = [3, 2, 2, 3]
val = 3

k = removeElement(l, val)
print(l[:k])
