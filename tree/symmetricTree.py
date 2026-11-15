"""
Problem: Symmetric Tree — Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). Key constraints: Node count is in [1, 1000] and -100 <= Node.val <= 100.
Source: LeetCode #101 (https://leetcode.com/problems/symmetric-tree/)
Solution Pattern: Depth-First Search (Simultaneous Mirror Traversal)
Complexity (My Solution):
    - Time: O(N) — Every node is compared once against its mirror counterpart.
    - Space: O(H) — Auxiliary call stack space scales with tree height H; O(log N) for balanced trees, O(N) for skewed trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, leftTree: TreeNode, rightTree: TreeNode):
        if not leftTree and not rightTree:
            return True

        if not leftTree or not rightTree:
            return False

        if leftTree.val != rightTree.val:
            return False

        # Check mirror reflection: compare outer subtrees (left-left vs right-right) and inner subtrees
        a = self.helper(leftTree.left, rightTree.right)
        b = self.helper(rightTree.left, leftTree.right)
        return a and b

    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root == None:
            return True

        return self.helper(root.left, root.right)
