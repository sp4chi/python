"""
Problem: Same Tree — Given the roots of two binary trees p and q, write a function to check if they are the same or not (structurally identical, and the nodes have the same value). Key constraints: Node count in each tree is in [0, 100] and -10^4 <= Node.val <= 10^4.
Source: LeetCode #100 (https://leetcode.com/problems/same-tree/)
Solution Pattern: Depth-First Search (Pre-order Traversal / Simultaneous Recursion)
Complexity (My Solution):
    - Time: O(N) — Where N is the minimum number of nodes between both trees; each node pair is checked once.
    - Space: O(H) — Auxiliary call stack space proportional to tree height H; O(log N) for balanced trees, O(N) for skewed trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False
        # Recursively verify structural identity and matching values across both child subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
