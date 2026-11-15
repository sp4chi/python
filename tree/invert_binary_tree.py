"""
Problem: Invert Binary Tree — Given the root of a binary tree, invert the tree (mirror reflection) and return its root. Key constraints: Node count is in [0, 100] and -100 <= Node.val <= 100.
Source: LeetCode #226 (https://leetcode.com/problems/invert-binary-tree/)
Solution Pattern: Depth-First Search (Post-order / Divide and Conquer)
Complexity (My Solution):
    - Time: O(N) — Visits each node once to invert and swap child subtrees.
    - Space: O(H) — Call stack depth corresponds to tree height H; O(log N) for balanced trees, O(N) for skewed trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        # Simultaneous tuple assignment swaps inverted left and right subtrees
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root
