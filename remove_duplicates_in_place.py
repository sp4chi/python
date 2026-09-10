from typing import List


def removeDuplicates(nums: List[int]) -> int:

    n = len(nums)

    left, right = (
        0,
        0,
    )

    for right in range(1, n):
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]

    return left + 1


l = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4]
k = removeDuplicates(l)
print(l)
