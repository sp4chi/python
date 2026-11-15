"""
Problem: Validate Binary Search Tree — Given the root of a binary tree, determine if it is a valid binary search tree (BST). Key constraints: Node count is in [1, 10^4] and -2^31 <= Node.val <= 2^31 - 1.
Source: LeetCode #98 (https://leetcode.com/problems/validate-binary-search-tree/)
Solution Pattern: Depth-First Search (Pre-order Range Validation with Lower/Upper Bounds)
Complexity (My Solution):
    - Time: O(N) — Every node is validated against bounded valid ranges once.
    - Space: O(H) — Auxiliary call stack space proportional to tree height H; O(log N) for balanced trees, O(N) for skewed trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        def helper(root, min_bound, max_bound):
            if not root:
                return True

            # Verify current node value strictly satisfies ancestor BST bounds
            if not (min_bound < root.val < max_bound):
                return False

            a = helper(root.left, min_bound, root.val)
            b = helper(root.right, root.val, max_bound)
            return a and b

        return helper(root, float("-inf"), float("inf"))
