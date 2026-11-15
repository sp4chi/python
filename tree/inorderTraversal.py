"""
Problem: Binary Tree Inorder Traversal — Given the root of a binary tree, return the inorder traversal of its nodes' values. Key constraints: Node count is in [0, 100] and -100 <= Node.val <= 100.
Source: LeetCode #94 (https://leetcode.com/problems/binary-tree-inorder-traversal/)
Solution Pattern: In-order Traversal (DFS / Left-Root-Right Recursion)
Complexity (My Solution):
    - Time: O(N) — Each node is visited once and appended to the output list.
    - Space: O(H) — Call stack depth scales with tree height H; O(log N) average, O(N) worst case.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, l):
        if root == None:
            return

        self.helper(root.left, l)
        # In-order visit: process left child, record root value, then process right child
        l.append(root.val)
        self.helper(root.right, l)

    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        l = []
        self.helper(root, l)
        return l
