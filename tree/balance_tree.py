"""
Problem: Convert Sorted Array to Binary Search Tree — Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree. Key constraints: 1 <= nums.length <= 10^4, -10^4 <= nums[i] <= 10^4, and nums is strictly sorted in ascending order.
Source: LeetCode #108 (https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)
Solution Pattern: Divide and Conquer / Binary Search (Pre-order Tree Construction)
Complexity (My Solution):
    - Time: O(N) — Every element in nums is visited once to construct a TreeNode.
    - Space: O(log N) — Call stack depth corresponds to the height of the balanced BST, which is bounded by O(log N).
"""

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

        # Pick middle element as root to ensure balanced left and right subtree heights
        mid = left + (right - left) // 2

        root = TreeNode(nums[mid])
        root.left = self.helper(left, mid - 1, nums)
        root.right = self.helper(mid + 1, right, nums)

        return root

    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:

        return self.helper(0, len(nums) - 1, nums)
