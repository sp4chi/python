"""
Problem: Diameter of Binary Tree — Given the root of a binary tree, return the length of the diameter (the length of the longest path between any two nodes in a tree, represented by the number of edges). Key constraints: Node count is in [1, 10^4] and -100 <= Node.val <= 100.
Source: LeetCode #543 (https://leetcode.com/problems/diameter-of-binary-tree/)
Solution Pattern: Post-order Traversal (DFS / Bottom-Up Depth Calculation)
Complexity (My Solution):
    - Time: O(N) — Each node is visited once to evaluate subtree heights.
    - Space: O(H) — Auxiliary call stack space scales with tree height H; O(log N) for balanced trees, O(N) for skewed trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    d = -1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = -1

        def helper(root):
            nonlocal d
            if not root:
                return 0

            a = helper(root.left)
            b = helper(root.right)

            h = max(a, b) + 1

            # Longest path through current node is the sum of left and right subtree depths
            d = max(d, a + b)

            return h

        helper(root)
        return d
