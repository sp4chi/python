"""
Problem: Maximum Depth of Binary Tree — Given the root of a binary tree, return its maximum depth (number of nodes along the longest path from root down to farthest leaf). Key constraints: Node count is in [0, 10^4] and -100 <= Node.val <= 100.
Source: LeetCode #104 (https://leetcode.com/problems/maximum-depth-of-binary-tree/)
Solution Pattern: Depth-First Search (Post-order Traversal)
Complexity (My Solution):
    - Time: O(N) — Visits each node once to compute subtree depths.
    - Space: O(H) — Auxiliary call stack space scales with tree height H; O(log N) for balanced trees, O(N) for skewed trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        # Max depth is 1 + maximum depth between left and right subtrees
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
