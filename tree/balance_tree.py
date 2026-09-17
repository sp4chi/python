# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, left: int, right: int, nums: List[int]) -> TreeNode | None:
        if left > right:
            return None

        mid = left + (right - left) // 2

        root = TreeNode(nums[mid])
        root.left = self.helper(left, mid - 1, nums)
        root.right = self.helper(mid + 1, right, nums)

        return root

    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:

        return self.helper(0, len(nums) - 1, nums)
